(async function () {
  const $ = s => document.querySelector(s);
  const esc = v => String(v == null ? '' : v).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const arr = v => Array.isArray(v) ? v : (v == null ? [] : [v]);
  const isUnknown = v => v == null || v === '' || v === 'unknown' || (Array.isArray(v) && (v.length === 0 || v.every(isUnknown)));
  const humanize = s => String(s).replace(/[_-]+/g, ' ').replace(/^\w/, c => c.toUpperCase());
  const REPO = 'https://github.com/Luisv8181/Global-Psychotherapy-Transcript-Data-Registry/blob/main/';

  const TYPE = { real: 'Real sessions', demonstration: 'Demonstration', peer_support: 'Peer support', synthetic: 'Synthetic', hybrid: 'Hybrid / derived', unknown: 'Unknown provenance' };
  const STRUCTURE = { multi_turn: 'Multi-turn dialogue', single_turn_qa: 'Single-turn Q&A', mixed: 'Mixed', unknown: 'Unknown' };
  const ACCESS = { open: 'Open', registration: 'Registration', 'research-agreement': 'Research agreement', institutional: 'Institutional', restricted: 'Restricted', 'metadata-only': 'Metadata only', unknown: 'Unknown' };
  const STATUS = { verified: 'Verified', 'partially-verified': 'Partially verified', unverified: 'Unverified', deprecated: 'Deprecated' };
  let langNames = null;
  try { langNames = new Intl.DisplayNames(['en'], { type: 'language' }); } catch (e) {}
  const langName = c => { if (!c || c === 'unknown') return 'Unknown'; try { return (langNames && langNames.of(c)) || c; } catch (e) { return c; } };

  const FACETS = [
    { key: 'type', title: 'Provenance', get: d => [d.dataset_type || 'unknown'], label: v => TYPE[v] || humanize(v), dot: true, open: true },
    { key: 'structure', title: 'Dialogue structure', get: d => [d.dialogue_structure || 'unknown'], label: v => STRUCTURE[v] || humanize(v), open: true },
    { key: 'access', title: 'Access', get: d => [(d.access && d.access.level) || 'unknown'], label: v => ACCESS[v] || humanize(v), open: true },
    { key: 'status', title: 'Verification', get: d => [d.status || 'unverified'], label: v => STATUS[v] || humanize(v) },
    { key: 'lang', title: 'Language', get: d => arr(d.languages).length ? arr(d.languages) : ['unknown'], label: langName },
  ];

  const state = { q: '', sort: 'completeness', sel: Object.fromEntries(FACETS.map(f => [f.key, new Set()])) };
  let data = [];
  try {
    data = await (await fetch('./data/datasets.json')).json();
  } catch (e) {
    $('#meta').textContent = 'The registry data could not be loaded.';
    return;
  }

  const haystack = d => [d.title, d.id, d.source_context, d.language_context, d.domain, arr(d.languages).map(langName).join(' '), arr(d.languages).join(' '),
    arr(d.therapy_modalities).join(' '), arr(d.clinical_topics).join(' '), arr(d.cultural_contexts).join(' '),
    d.geography ? arr(d.geography.countries).join(' ') + ' ' + arr(d.geography.regions).join(' ') : ''].join(' ').toLowerCase();
  data.forEach(d => { d._hay = haystack(d); });

  function matches(d, skip) {
    if (state.q && !d._hay.includes(state.q)) return false;
    return FACETS.every(f => f.key === skip || state.sel[f.key].size === 0 || f.get(d).some(v => state.sel[f.key].has(v)));
  }

  function renderStats() {
    const langs = new Set(data.flatMap(d => arr(d.languages)).filter(l => l && l !== 'unknown'));
    const real = data.filter(d => d.dataset_type === 'real').length;
    fetch('./data/videos.json').then(r => r.ok ? r.json() : []).catch(() => []).then(v => {
      const items = [[data.length, 'datasets'], [langs.size, 'languages'], [real, 'real-session datasets'], [v.length, 'catalogued videos']];
      $('#stats').innerHTML = items.map(([n, l]) => `<div class="stat"><b>${n}</b><span>${esc(l)}</span></div>`).join('');
    });
  }

  function renderFacets() {
    $('#facets').innerHTML = FACETS.map(f => {
      const base = data.filter(d => matches(d, f.key));
      const counts = {};
      data.forEach(d => f.get(d).forEach(v => { counts[v] = counts[v] || 0; }));
      base.forEach(d => f.get(d).forEach(v => { counts[v] += 1; }));
      const vals = Object.keys(counts).sort((a, b) => (a === 'unknown') - (b === 'unknown') || counts[b] - counts[a] || f.label(a).localeCompare(f.label(b)));
      const open = f.open || state.sel[f.key].size ? ' open' : '';
      return `<details${open}><summary>${esc(f.title)}</summary><div class="facet">` + vals.map(v => {
        const id = `f-${f.key}-${v}`.replace(/[^\w-]/g, '_');
        const checked = state.sel[f.key].has(v) ? ' checked' : '';
        const zero = counts[v] === 0 && !checked ? ' class="zero"' : '';
        return `<label${zero} for="${id}"><input type="checkbox" id="${id}" data-facet="${f.key}" value="${esc(v)}"${checked}>` +
          (f.dot ? `<i class="dot ${esc(v)}"></i>` : '') + `${esc(f.label(v))}<span class="count">${counts[v]}</span></label>`;
      }).join('') + '</div></details>';
    }).join('');
  }

  function renderChips() {
    const chips = [];
    FACETS.forEach(f => state.sel[f.key].forEach(v => chips.push(`<button class="chip-btn" type="button" data-facet="${f.key}" data-value="${esc(v)}">${esc(f.label(v))} ✕</button>`)));
    $('#chips').innerHTML = chips.join('');
  }

  function sortRows(rows) {
    const year = d => d.publication_year || d.release_year || 0;
    const num = d => typeof d.sessions === 'number' ? d.sessions : -1;
    const ratio = d => d._completeness ? d._completeness.ratio : 0;
    const by = {
      completeness: (a, b) => ratio(b) - ratio(a) || a.title.localeCompare(b.title),
      title: (a, b) => a.title.localeCompare(b.title),
      year: (a, b) => year(b) - year(a) || a.title.localeCompare(b.title),
      sessions: (a, b) => num(b) - num(a) || a.title.localeCompare(b.title),
    }[state.sort];
    return rows.slice().sort(by);
  }

  function badges(d) {
    const t = d.dataset_type || 'unknown';
    const out = [`<span class="badge type"><i class="dot ${esc(t)}"></i>${esc(TYPE[t] || humanize(t))}</span>`];
    if (d.dialogue_structure && d.dialogue_structure !== 'unknown') out.push(`<span class="badge">${esc(STRUCTURE[d.dialogue_structure] || d.dialogue_structure)}</span>`);
    const langs = arr(d.languages).filter(l => l !== 'unknown');
    if (langs.length) out.push(`<span class="badge">${esc(langs.slice(0, 3).map(langName).join(', '))}${langs.length > 3 ? ' +' + (langs.length - 3) : ''}</span>`);
    if (typeof d.sessions === 'number') out.push(`<span class="badge">${d.sessions.toLocaleString('en')} ${d.dialogue_structure === 'single_turn_qa' ? 'items' : 'sessions'}</span>`);
    const acc = d.access && d.access.level;
    if (acc && acc !== 'unknown') out.push(`<span class="badge">Access: ${esc(ACCESS[acc] || humanize(acc))}</span>`);
    const lic = d.license && d.license.type;
    if (lic && lic !== 'unknown') out.push(`<span class="badge">License: ${esc(lic === 'none-selected' ? 'none selected' : lic)}</span>`);
    return out.join('');
  }

  function renderResults() {
    const rows = sortRows(data.filter(d => matches(d)));
    const active = Object.values(state.sel).some(s => s.size) || state.q;
    $('#meta').textContent = `${rows.length} of ${data.length} datasets` + (active ? ' match your filters' : '');
    $('#results').innerHTML = rows.length ? rows.map(d => {
      const c = d._completeness || { documented: 0, total: 12, ratio: 0 };
      const st = d.status || 'unverified';
      return `<button class="row" type="button" data-id="${esc(d.id)}" aria-expanded="false">
        <div><h3>${esc(d.title)}</h3><p>${esc(d.source_context || 'No source-context summary recorded.')}</p><div class="badges">${badges(d)}</div></div>
        <div class="completeness"><span class="${st === 'verified' ? 'status-verified' : ''}">${esc(STATUS[st] || st)}</span>
          <div class="meter" role="img" aria-label="${c.documented} of ${c.total} core fields documented"><i style="width:${Math.round(c.ratio * 100)}%"></i></div>
          ${c.documented} of ${c.total} core fields documented</div>
      </button>`;
    }).join('') : '<div class="empty">No datasets match these filters. <button class="linkish" type="button" data-clear>Clear all filters</button></div>';
  }

  function render() { renderFacets(); renderChips(); renderResults(); }

  // Detail drawer
  const link = u => /^https?:\/\//.test(u) ? `<a href="${esc(u)}" target="_blank" rel="noreferrer">${esc(u.replace(/^https?:\/\/(www\.)?/, ''))} ↗</a>` : esc(u);
  function value(v) {
    if (isUnknown(v)) return '<span class="unknown-val">Unknown</span>';
    if (typeof v === 'boolean') return v ? 'Yes' : 'No';
    if (Array.isArray(v)) return v.map(x => typeof x === 'string' ? link(x) : value(x)).join('<br>');
    if (typeof v === 'object') return Object.entries(v).filter(([k]) => !k.startsWith('_')).map(([k, x]) => `<b>${esc(humanize(k))}:</b> ${value(x)}`).join('<br>');
    if (typeof v === 'string') return link(v);
    return esc(v);
  }
  function section(title, rows) {
    return `<section class="dl-section"><h3>${esc(title)}</h3><dl>` +
      rows.map(([k, v]) => `<div><dt>${esc(k)}</dt><dd>${value(v)}</dd></div>`).join('') + '</dl></section>';
  }

  let lastFocus = null;
  function openDrawer(id, push) {
    const d = data.find(x => x.id === id);
    if (!d) return;
    const c = d._completeness || { unknown_fields: [] };
    const lic = d.license || {};
    $('#drawer-body').innerHTML = `
      <div class="badges">${badges(d)}</div>
      <h2 id="drawer-title">${esc(d.title)}</h2>
      <div class="drawer-links">
        ${/^https?:/.test(d.canonical_url || '') ? `<a href="${esc(d.canonical_url)}" target="_blank" rel="noreferrer">Canonical source ↗</a>` : ''}
        ${d._source_file ? `<a href="${esc(REPO + d._source_file)}" target="_blank" rel="noreferrer">Registry record on GitHub ↗</a>` : ''}
      </div>` +
      (d.notes ? `<section class="dl-section"><h3>Notes</h3><div class="note-box">${esc(d.notes)}</div></section>` : '') +
      section('Provenance', [['Status', STATUS[d.status] || d.status], ['Dataset type', TYPE[d.dataset_type] || d.dataset_type], ['Dialogue structure', STRUCTURE[d.dialogue_structure] || d.dialogue_structure], ['Source context', d.source_context], ['Generation', d.generation], ['Domain', d.domain && humanize(d.domain)]]) +
      section('Coverage', [['Languages', arr(d.languages).map(langName)], ['Language context', d.language_context], ['Geography', d.geography], ['Therapy modalities', arr(d.therapy_modalities).map(humanize)], ['Topics', arr(d.clinical_topics).map(humanize)], ['Sessions', typeof d.sessions === 'number' ? d.sessions.toLocaleString('en') : d.sessions], ['Longitudinal', d.longitudinal], ['Annotations', arr(d.annotations).map(humanize)]]) +
      section('Access, license and privacy', [['Access', d.access && d.access.level && (ACCESS[d.access.level] || d.access.level)], ['Requirements', d.access && d.access.requirements], ['Redistribution', d.redistribution && humanize(d.redistribution)], ['License', lic.type === 'none-selected' ? 'No license selected' : lic.type], ['License confirmed', lic.verified], ['License read at', lic.source], ['License notes', lic.notes], ['Privacy', d.privacy]]) +
      section('Evidence', [['Primary sources', d.evidence && d.evidence.primary_sources], ['Publications', d.evidence && (d.evidence.supporting_publications || d.evidence.supporting_sources)], ['Published', d.publication_year], ['Released', d.release_year], ['Last verified', d.last_verified], ['Not yet established', c.unknown_fields && c.unknown_fields.length ? c.unknown_fields.join(', ') : 'Nothing among the core fields']]);
    lastFocus = document.activeElement;
    $('#drawer').classList.add('open'); $('#scrim').classList.add('open');
    $('#drawer').setAttribute('aria-hidden', 'false');
    document.querySelectorAll('.row').forEach(r => r.setAttribute('aria-expanded', String(r.dataset.id === id)));
    $('#drawer-body').scrollTop = 0;
    $('#close').focus();
    if (push) history.replaceState(null, '', '#' + encodeURIComponent(id));
  }
  function closeDrawer() {
    $('#drawer').classList.remove('open'); $('#scrim').classList.remove('open');
    $('#drawer').setAttribute('aria-hidden', 'true');
    document.querySelectorAll('.row').forEach(r => r.setAttribute('aria-expanded', 'false'));
    history.replaceState(null, '', location.pathname + location.search);
    if (lastFocus) lastFocus.focus();
  }

  // Events
  $('#search').addEventListener('input', e => { state.q = e.target.value.trim().toLowerCase(); render(); });
  $('#sort').addEventListener('change', e => { state.sort = e.target.value; renderResults(); });
  $('#facets').addEventListener('change', e => {
    const t = e.target; if (!t.dataset.facet) return;
    t.checked ? state.sel[t.dataset.facet].add(t.value) : state.sel[t.dataset.facet].delete(t.value);
    render();
  });
  const clearAll = () => { FACETS.forEach(f => state.sel[f.key].clear()); state.q = ''; $('#search').value = ''; render(); };
  $('#clear').addEventListener('click', clearAll);
  $('#chips').addEventListener('click', e => { const b = e.target.closest('[data-facet]'); if (!b) return; state.sel[b.dataset.facet].delete(b.dataset.value); render(); });
  $('#results').addEventListener('click', e => {
    if (e.target.closest('[data-clear]')) return clearAll();
    const r = e.target.closest('.row'); if (r) openDrawer(r.dataset.id, true);
  });
  $('#filters-toggle').addEventListener('click', e => {
    const open = $('#filters').classList.toggle('open');
    e.currentTarget.setAttribute('aria-expanded', String(open));
  });
  $('#close').addEventListener('click', closeDrawer);
  $('#scrim').addEventListener('click', closeDrawer);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && $('#drawer').classList.contains('open')) closeDrawer(); });

  renderStats();
  render();
  if (location.hash.length > 1) openDrawer(decodeURIComponent(location.hash.slice(1)), false);
})();
