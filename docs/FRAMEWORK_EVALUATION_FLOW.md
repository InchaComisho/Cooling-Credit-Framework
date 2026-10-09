# Cooling Credit Framework Evaluation Flow

[日本語版はこちら / Japanese version](FRAMEWORK_EVALUATION_FLOW_ja.md)

This document defines a practical evaluation flow for applying the **Cooling Credit Framework**.

It positions this repository as the procedural layer between the formal definition and real-world implementation.

- **Definition layer:** [Cooling-Credit-Definition](https://github.com/InchaComisho/Cooling-Credit-Definition)
- **Framework layer:** this repository
- **Implementation layer:** [Cooling-Credit-Implementation-Portfolio](https://github.com/InchaComisho/Cooling-Credit-Implementation-Portfolio)
- **Finance layer:** [Cooling-Credit-Implementation-and-Finance-Model](https://github.com/InchaComisho/Cooling-Credit-Implementation-and-Finance-Model)

In short:

> **Definition defines what a Cooling Credit is.**  
> **Framework determines whether an activity qualifies.**  
> **Implementation tests it in the real world.**  
> **Finance designs how it can be funded and maintained.**

---

## 1. Purpose of the Evaluation Flow

A Cooling Credit must not be issued merely because an activity sounds environmentally beneficial.

It should pass a structured evaluation process showing that it produces one or more of the following verified outcomes:

- direct cooling;
- heat-load reduction;
- water-cycle cooling recovery;
- latent heat transport restoration;
- soil moisture and evapotranspiration recovery;
- ocean-atmosphere heat-exchange recovery;
- restoration of natural cooling functions;
- measurable reduction of heat-stress or cooling demand.

This flow is designed to prevent concept dilution, greenwashing, over-crediting, and confusion with Carbon Credits, Sunshade Credits, Reflect Credits, Adaptation Credits, or Resilience Credits.

---

## 2. Evaluation Gate Structure

The proposed evaluation process consists of seven gates.

| Gate | Question | Result |
|---|---|---|
| Gate 1: Category Check | Is the primary mechanism cooling or natural cooling-function restoration? | If no, classify elsewhere |
| Gate 2: Boundary Check | Is it distinct from carbon accounting, solar shielding, and reflectivity-only measures? | If no, exclude or reclassify |
| Gate 3: Baseline Check | Is there a credible baseline or control condition? | If no, require pilot data |
| Gate 4: MRV Check | Can the cooling outcome be measured, reported, and verified? | If no, do not issue credits |
| Gate 5: Risk Check | Are humidity, water stress, ecological risk, and rebound risk managed? | If no, apply penalties or reject |
| Gate 6: Attribution Check | Can the cooling effect be attributed to the intervention? | If no, classify as unverified |
| Gate 7: Duration Check | Is the cooling effect temporary, seasonal, recurring, or durable? | Determines validity period |

Only projects that pass these gates should proceed to provisional scoring or credit estimation.

---

## 3. Gate 1: Category Check

The first question is whether the activity belongs inside the Cooling Credit category at all.

A project may be considered if its primary verified outcome includes:

- lower air temperature;
- lower land-surface temperature;
- lower water or sea-surface temperature;
- lower WBGT or heat-stress pressure;
- reduced artificial waste heat;
- restored soil moisture;
- restored evapotranspiration;
- restored hydrological buffering;
- restored ocean mixing or oxygenation connected to thermal regulation;
- reduced cooling-energy demand caused by verified environmental cooling.

A project should not proceed as a Cooling Credit if its primary mechanism is only:

- CO2 accounting;
- emission offsetting;
- sunlight blocking;
- surface whitening;
- albedo increase;
- general disaster preparedness;
- general adaptation without measurable cooling.

These may be valuable, but they should be classified under other credit categories unless direct cooling outcomes are separately verified.

---

## 4. Gate 2: Boundary Check

The boundary check protects the meaning of the term **cooling**.

Cooling Credit classification should be reserved for interventions that reduce existing heat load or restore natural cooling processes.

| Mechanism | Default treatment |
|---|---|
| Direct temperature reduction | Eligible for Cooling Credit evaluation |
| Water-cycle restoration | Eligible for Cooling Credit evaluation |
| Soil moisture and evapotranspiration recovery | Eligible for Cooling Credit evaluation |
| Ocean-atmosphere heat exchange support | Eligible under strict monitoring |
| CO2 reduction only | Carbon Credit, not Cooling Credit by default |
| Solar radiation blocking | Sunshade Credit, not Cooling Credit by default |
| Albedo or reflectivity increase only | Reflect Credit, not Cooling Credit by default |
| Disaster preparedness only | Resilience Credit, not Cooling Credit by default |
| Vulnerability reduction only | Adaptation Credit, not Cooling Credit by default |

If a non-cooling category also produces measurable cooling, only the cooling outcome may be evaluated separately.

---

## 5. Gate 3: Baseline Check

A Cooling Credit claim requires a baseline.

A baseline may be established through:

- pre-intervention measurement;
- untreated control areas;
- historical averages;
- remote-sensing comparison;
- seasonal correction models;
- paired site comparison;
- simulation-assisted estimation for pilot design.

A weak baseline should not automatically reject a pilot, but it should prevent formal credit issuance until measurement improves.

---

## 6. Gate 4: MRV Check

MRV means **Measurement, Reporting, and Verification**.

Required indicators may include:

- air temperature;
- surface temperature;
- water or sea-surface temperature;
- WBGT;
- humidity;
- soil moisture;
- evapotranspiration;
- heat flux;
- water retention;
- vegetation recovery;
- cooling-energy demand;
- waste-heat reduction;
- ocean mixing indicators;
- dissolved oxygen;
- ecological response indicators.

MRV should define:

1. measurement boundary;
2. baseline method;
3. monitoring period;
4. measurement instruments;
5. reporting interval;
6. uncertainty range;
7. third-party verification method;
8. risk and penalty conditions;
9. validity period of the credit.

---

## 7. Gate 5: Risk Check

Cooling must not be pursued at any cost.

The following risks should be checked before credit issuance:

| Risk | Example | Response |
|---|---|---|
| Humidity risk | Mist cooling may raise humidity in humid climates | Evaluate WBGT, not air temperature alone |
| Water stress risk | Cooling water may compete with drinking water or ecosystem flow | Prefer rainwater, reclaimed water, greywater, or circulated water |
| Ecological risk | Large-scale greening or ocean interventions may alter ecosystems | Require regional suitability and monitoring |
| Rebound risk | Efficiency gains may increase total use | Monitor net heat-load effect |
| Over-crediting risk | Short-term cooling may be overstated | Use duration and uncertainty penalties |
| Leakage risk | Heat or water stress may shift elsewhere | Evaluate system boundary effects |

---

## 8. Gate 6: Attribution Check

The cooling outcome must be attributable to the intervention.

Attribution may be supported by:

- before-after comparison;
- control-site comparison;
- sensor networks;
- satellite observation;
- modeled counterfactuals;
- weather normalization;
- hydrological monitoring;
- energy-use monitoring;
- independent verification.

If attribution is uncertain, the project should remain in pilot or provisional status.

---

## 9. Gate 7: Duration Check

Cooling effects differ in duration.

| Duration type | Example | Credit treatment |
|---|---|---|
| Instant / temporary | mist cooling during operation | short validity period |
| Daily recurring | building exhaust reduction | operational validity |
| Seasonal | vegetation or soil moisture recovery | seasonal verification |
| Multi-year | forest, wetland, watershed restoration | long-term monitoring required |
| Infrastructure-based | water-circulation city systems | maintenance-linked validity |
| Ocean or regional systems | ocean circulation support | strict long-term monitoring |

The validity period of a Cooling Credit should match the measured duration of the cooling effect.

---

## 10. Provisional Scoring Structure

After passing the gates, a project may be scored provisionally.

A simplified structure is:

```text
Cooling Credit Score =
  Thermal Reduction
+ Water-Cycle Recovery
+ Evapotranspiration Recovery
+ Heat-Stress Reduction
+ Cooling-Demand Reduction
+ Ecological Cooling Recovery
- Water-Stress Penalty
- Humidity-Risk Penalty
- Ecological-Risk Penalty
- Attribution-Uncertainty Penalty
- Duration-Uncertainty Penalty
```

This score should be used for pilot comparison, prioritization, and institutional design. It should not be treated as a formal financial product unless governance, legal status, and verification methods are separately established.

---

## 11. Decision Outcomes

The evaluation flow can produce five outcomes.

| Outcome | Meaning |
|---|---|
| Eligible | Meets Cooling Credit definition and MRV conditions |
| Provisionally eligible | Promising, but needs stronger measurement or longer monitoring |
| Reclassify | Valuable, but belongs under another credit category |
| Exclude | Does not produce measurable cooling or cooling-function recovery |
| Monitor only | Too uncertain for crediting but useful for research or pilot data |

---

## 12. Relationship to the Definition Repository

This framework should be interpreted under the definition and boundary rules proposed in:

- [Cooling-Credit-Definition](https://github.com/InchaComisho/Cooling-Credit-Definition)
- [Cooling Credit Standard Draft](https://github.com/InchaComisho/Cooling-Credit-Definition/blob/main/docs/COOLING_CREDIT_STANDARD_DRAFT.md)
- [MRV Requirements](https://github.com/InchaComisho/Cooling-Credit-Definition/blob/main/docs/MRV_REQUIREMENTS.md)
- [Eligible Activities](https://github.com/InchaComisho/Cooling-Credit-Definition/blob/main/docs/ELIGIBLE_ACTIVITIES.md)
- [Excluded Categories](https://github.com/InchaComisho/Cooling-Credit-Definition/blob/main/docs/EXCLUDED_CATEGORIES.md)
- [Terminology](https://github.com/InchaComisho/Cooling-Credit-Definition/blob/main/docs/TERMINOLOGY.md)

The Definition repository defines the conceptual boundary.  
This Framework repository provides the evaluation process.

---

## 13. Summary

A Cooling Credit should pass through a structured evaluation process before it is treated as a verified cooling contribution.

The key question is not:

```text
Does this look environmentally good?
```

The key question is:

```text
Did it measurably reduce heat load or restore a natural cooling function, under a credible baseline, MRV process, and risk-control structure?
```

This is the central role of the Cooling Credit Framework.

---

## Author

Master / inchacomusho / InchaComisho

An independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and proposer of the academic framework of Natural Complementary Science.  
Definer of the Cooling Credit Framework, and founder and original author of the Natural Cooling Value Evaluation Protocol.  
Definer and systematizer of the causal structure of global warming and its complete solution.

Master presents global warming not merely as a problem of CO₂ concentration, but as an integrated failure involving forest loss, soil degradation, disruption of water circulation, weakening of water phase-transition processes, weakening of atmospheric circulation, ocean circulation, food circulation and organic matter circulation, weakening of evapotranspiration, cloud formation and rainfall circulation, and the shutdown of natural cooling feedbacks.  
The proposed solution connects emission reduction, recovery of carbon fixation sources, physical cooling, reactivation of natural cooling functions, MRV, Cooling Credit, and Civilization OS into an open public framework.

Master publicly develops and shares work through NOTE, GitHub, and other public media, centered on natural-law philosophy, planetary circulation restoration, and co-creation with AI.

## License

CC BY 4.0

This article is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).  
Sharing, redistribution, translation, adaptation, and reuse are permitted as long as proper attribution is given.