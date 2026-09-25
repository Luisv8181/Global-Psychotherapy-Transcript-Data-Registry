# Global Coverage Model

The registry's coverage model is multidimensional.

## Coverage vector

A dataset can be represented as:

country × region × source_language × dialect × cultural_context × therapy_modality × population × age_group × clinical_topic × longitudinal × access × privacy

The registry should not reduce this vector to a single global-coverage score.

## Important distinctions

### Source language vs released language

Record both. A Japanese corpus translated into English remains Japanese-source data.

### Country vs language

Do not infer country from language.

### Culture vs country

A country can contain multiple cultural and linguistic contexts. A diaspora dataset may span countries.

### Real vs synthetic

Synthetic dialogue can be valuable, but it must remain distinguishable from real therapy.

### Access vs license

A publicly visible webpage does not necessarily grant redistribution rights.

### Deidentified vs privacy-tested

Removal of explicit identifiers is not equivalent to demonstrated resistance to contextual re-identification.

## Coverage questions

The registry should eventually answer which countries have real therapy dialogue datasets, which languages have original-source therapy transcripts, which languages are represented only through translation, which regions have longitudinal therapy data, which modalities are represented outside North America and Europe, which populations are underrepresented, which datasets have adversarial privacy evaluation, which datasets have documented consent or governance, and where the largest evidence gaps are.

## Dashboard concept

Future views should support: World map → country → language → dataset → therapy modality → access/privacy → evidence.

And: Language → country → culture → modality → longitudinal → research availability.

Unknown values should remain visible rather than being silently excluded.
