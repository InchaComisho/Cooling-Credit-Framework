# نموذج أثر الحجم ودرجة الحرارة لأرصدة التبريد

[← العودة إلى README_ar.md](../../README_ar.md)

---

## اللغات / Languages

- [日本語](README_ja.md)
- [English](README.md)
- [العربية](README_ar.md)

---

## نظرة عامة

هذا النموذج هو محاكاة مبسطة للمقارنة بين أحجام مختلفة من إجراءات أرصدة التبريد وتأثيرها المحتمل على مؤشرات التبريد المحلية والإقليمية.

يشمل النموذج مراوح الرذاذ فوق الصوتي المركزية، وإعادة تجهيز المرافق العامة، وتحويل النفايات العضوية إلى دبال، والتخضير الحضري، وتجديد الغابات، واستعادة التربة، ودعم دوران المحيط.

هذا ليس نموذجًا للتنبؤ بالمناخ. إنه نموذج أولي لتحليل الحساسية، يساعد المستثمرين والبلديات والشركات والباحثين على مقارنة حجم التنفيذ، والاستثمار، وأثر التبريد، ونقاط التبريد.

---

## الهدف

```text
حجم التنفيذ
↓
كمية إجراءات التبريد
↓
خفض الحمل الحراري
↓
خفض درجة الحرارة وWBGT والطلب على التبريد
↓
نقاط التبريد
↓
أرصدة تبريد أولية
↓
قرارات الاستثمار والتنفيذ
```

---

## أعمدة الإدخال

يستخدم `example_inputs.csv` الأعمدة التالية.

| العمود | المعنى |
|---|---|
| scenario | اسم السيناريو |
| scale_level | مستوى حجم التنفيذ |
| project_area_ha | مساحة المشروع بالهكتار |
| mist_fan_units | عدد وحدات مراوح الرذاذ |
| public_facility_retrofits | عدد تجهيزات المرافق العامة أو النقل |
| organic_waste_tons_year | كمية النفايات العضوية المعالجة سنويًا |
| urban_greening_ha | مساحة التخضير الحضري بالهكتار |
| forest_regeneration_ha | مساحة تجديد الغابات بالهكتار |
| soil_restoration_ha | مساحة استعادة التربة بالهكتار |
| ocean_circulation_units | وحدات دعم دوران المحيط |
| investment_usd_million | الاستثمار بالمليون دولار |

---

## المخرجات

تشمل المخرجات الرئيسية:

- تقدير خفض درجة حرارة الهواء،
- تقدير خفض درجة حرارة السطح،
- تقدير خفض WBGT،
- تقدير خفض الطلب على التبريد،
- مؤشر استعادة دورة المياه،
- مؤشر استعادة النظام البيئي،
- مؤشر خفض مخاطر الحرارة،
- نقاط التبريد،
- أرصدة تبريد أولية،
- أرصدة أولية لكل مليون دولار.

---

## طريقة التشغيل

```bash
cd simulations/cooling_credit_scale_temperature_model
python cooling_credit_scale_temperature_model.py
```

يتم حفظ النتائج في `outputs/`.

```text
outputs/
├─ scale_temperature_results.csv
├─ scale_vs_air_temperature_reduction.png
├─ scale_vs_wbgt_reduction.png
├─ scale_vs_cooling_demand_reduction.png
├─ scale_vs_cooling_score.png
├─ investment_vs_cooling_credits.png
└─ investment_vs_temperature_reduction.png
```

---

## سيناريوهات المثال

يتضمن ملف CSV الأولي خمسة مستويات:

1. Small pilot
2. District program
3. Municipal deployment
4. Regional watershed program
5. National portfolio

يسمح ذلك بمقارنة التنفيذ التجريبي، والبلدي، والإقليمي، والوطني.

---

## تنبيه مهم

هذا النموذج ليس نموذجًا رسميًا لإصدار الأرصدة.

ولا يقدم تنبؤًا مناخيًا، أو نموذجًا حضريًا للأرصاد، أو نموذجًا للمحيط، أو ضمانًا للتأثير الصحي، أو ضمانًا لعائد الاستثمار.

هدفه هو تصور العلاقة بين حجم التنفيذ ومؤشرات أثر التبريد، وتقديم أداة مقارنة أولية لتصميم نظام أرصدة التبريد، ونماذج الأعمال، والمشاريع التجريبية، وبرامج البلديات، ومناقشات الاستثمار.

---

## روابط ذات صلة

- [Cooling Credit Framework](../../README_ar.md)
- [Cooling Credit Score Estimator](../cooling_credit_score_estimator/README_ar.md)
- [نماذج أعمال أرصدة التبريد](../../docs/business_models/BUSINESS_MODEL_INDEX_ar.md)
- [الدعم والتعاون والتنفيذ](../../docs/SUPPORT_AND_COLLABORATION_ar.md)

---

## الفكرة الأصلية

Master / inchacomusho / InchaComisho

دعم الهيكل والتوثيق وتصميم الكود: G (ChatGPT)
