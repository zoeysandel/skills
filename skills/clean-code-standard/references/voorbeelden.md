# Voorbeelden: slecht en goed naast elkaar

De voorbeelden illustreren de standaard met een evaluatieharnas voor subsidiegegevens.

## Namen

Slecht:
```
eval/
├── f2eval/
├── r8/detect.py
├── r9/ist.py
├── r10/r10/controls.py
└── sil/akorda_inventaris.py
```

Goed:
```
src/duo_eval/
├── services/missing_decision_detector.py
├── services/afas_actuals.py
├── evaluation/duo_export_checks/amount_checks.py
└── engines/artifact_engine.py
```
Het werklabel staat in de README: `| R8 | missing_decision_detector.py | beschikkingen die de engine verwacht maar niet in de export staan |`.

## Eén statement per regel en geen magische waarden

Slecht:
```python
def nld(s): d, m, y = s.strip().split("-"); return date(int(y), int(m), int(d))
besl = defaultdict(set); onderw = set(); scholen = set(); bad_per = 0; neg = set()
extras = base["beslissingRows"][277:]
```

Goed:
```python
def parse_dutch_date(text: str) -> date:
    day, month, year = text.strip().split("-")
    return date(int(year), int(month), int(day))

extra_decisions = payload.rows[payload.export_row_count:]
```

## Een begrip als klasse

Slecht:
```python
totals[key] = [0, 0, 0, 0]   # engine per maand, model per maand, engine cum, model cum
totals[key][1] += row.amount
```

Goed:
```python
@dataclass
class SpreadTotals:
    engine_monthly: Decimal = ZERO
    model_monthly: Decimal = ZERO
    engine_cumulative: Decimal = ZERO
    model_cumulative: Decimal = ZERO
```

## Extern systeem achter een interface

Slecht: het tabblad Mutaties wordt in drie files los gelezen, elk met eigen kolomnummers en eigen tekenafspraak.

Goed:
```python
class AfasMutationSource(Protocol):
    def mutations(self, account: str, year: int) -> list[AfasMutation]: ...

class ModelSheetMutationSource:
    """Reads AFAS mutations from the Mutaties tab of a client model."""
```
Een latere API-koppeling wordt een tweede implementatie. Geen eval verandert.

## Een eval die aantoonbaar werkt

Slecht: een controle die bij nul ingelezen rijen "pass" geeft, en een zelftest die alleen aantallen print.

Goed:
```python
class Evaluation(ABC):
    name: str
    reason: str

    def evaluate(self, cases: Sequence[Case]) -> EvalResult:
        if not cases:
            return EvalResult.not_tested(self.name, "no input rows")
        return self._evaluate(cases)
```
```python
def test_monthly_spread_eval_catches_engine_without_month_rounding():
    engine = NoMonthRounding(ReferenceEngine())
    result = MonthlySpreadEval().evaluate(run(engine, sample_decisions()))
    assert result.failed
```

## Varianten als klasse, niet als string-vlag

Slecht:
```python
def database_rows(decs, cfg, mutant=None):
    ...
    split = {...} if mutant == "geen_afroming" else verdeling(dec, cfg)
```

Goed:
```python
class NoSkimming(SubsidyEngine):
    """Broken on purpose: puts the whole amount on one cost centre. Used to prove evals catch it."""
    def __init__(self, engine: SubsidyEngine): ...
```

## Fouten luid maken

Slecht:
```python
if len(r) != len(h): continue
try: ...
except Exception: pass
```

Goed:
```python
if len(row) != len(header):
    raise MalformedRowError(line_number, expected=len(header), found=len(row))
```
