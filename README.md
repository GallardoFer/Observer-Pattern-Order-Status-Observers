# Order Status Observers — Starter

## Your task
1. Introduce an `Observer` contract and subscription.
2. Adapt `CustomerNotifier` and `AuditObserver`.
3. Add `AnalyticsObserver` without changing `OrderStatus` notification logic.
4. Add/update one focused test.
5. Explain one lifecycle/coupling cost.


## Local setup

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Course conventions

- Python is only the implementation language for the exercise; the design roles are language-agnostic.
- Use an explicit object-oriented design.
- Keep one main class per source file.

