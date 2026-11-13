# Reproducibility

## Seed

The dataset generator uses a fixed seed:

20261022

## Regeneration

Run:

```bash
python generate.py
```

## Expected Result

Using the same seed value generates the same synthetic dataset structure and records every time.

## Validation

- Fixed random seed
- Consistent ID generation
- Deterministic output structure
