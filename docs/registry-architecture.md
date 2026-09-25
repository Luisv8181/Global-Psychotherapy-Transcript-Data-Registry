# Registry Architecture

```text
                 +-----------------------------+
                 |  Primary dataset sources    |
                 |  repositories / publishers  |
                 |  institutions / papers     |
                 +-------------+---------------+
                               |
                               v
                    +----------------------+
                    | Evidence + verifier  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Canonical YAML       |
                    | dataset records      |
                    +----------+-----------+
                               |
                +--------------+--------------+
                |                             |
                v                             v
       +----------------+            +----------------+
       | JSON Schema    |            | Search/index   |
       | validation     |            | layer          |
       +----------------+            +-------+--------+
                                            |
                          +-----------------+----------------+
                          |                                  |
                          v                                  v
                 Research discovery                  Future web/API
```

The authoritative layer is the evidence-backed dataset record. Search, exports, visualizations, and future APIs are derived views.

The registry never needs to possess the underlying transcript to describe the dataset responsibly.
