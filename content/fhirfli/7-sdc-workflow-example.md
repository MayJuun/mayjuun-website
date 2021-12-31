---
title: "SDC Workflow Example"
date: 2021-12-03T20:38:59Z
type: post
author: Grey Faulkenberry, MD MPH
tags: ["FHIR®","SDC", "Questionnaire", "QuestionnaireResponse", "Structured Data Capture"]
---
## Structured Data Capture (SDC)

As usual, the HL7 website has a lot to say on the topic of [SDC](http://hl7.org/fhir/uv/sdc/2019May/workflow.html), and I DO advise you to read through it because it's very helpful. However, where I thought I might be able value is with some additional examples.

All of these examples are from a project I'm currently involved with for [New Jersey Integrated Care for Kids](https://www.zanenetworks.com/zane-networks-mayjuun-receive-contract-for-the-needs-assessment-tool-solution-for-new-jerseys-inck-project/). The idea behind this project is that a clinician (social worker, teacher, etc.), would like to perform a needs assessment on a pediatric patient. They request the assesment, then we create a Task using a PlanDefinition that includes multiple questionnaires appropriate for that age group. They are sent the questionnaires, complete them, and the Task is completed and updated with the QuestionnaireResponses as well as a MeasureReport for overall scoring. It took a while to try and ensure I had the correct workflow and all of the correct resources. I figured I would document that all here to get feedback and offer an example to anyone who might need one.

### ServiceRequest

While the request can come from anyone (with the ability to do such a thing), we represent it on our server using a ServiceRequest. A sample ServiceRequest is displayed below:

{{< code json >}}
{
    "resourceType": "ServiceRequest",
    "priority": "routine",
    "status": "active",
    "intent": "instance-order",
    "instantiatesUri": [
        "PlanDefinition/4840239b-4da6-4fa6-b8d6-4a1b1a7140af"
    ],
    "requester": {
        "reference": "Organization/fd7b5daa-3a00-4bb5-bef2-c1d5ed375c6e"
    },
    "subject": {
        "reference": "Patient/8a968030-9d13-4938-b722-bc957e85088a"
    },
    "performer": {
        "reference": "RelatedPerson/8a968031-9d13-4938-b722-bc957e85088a"
    }
}
{{< /code >}}  

As usual, not all fields are mandatory. The PlanDefinition is decided based on the patient's age. The requester can be an Organization or a Practitioner (for our use case). We include both the subject and the performer since we are dealing with pediatric patients.

### PlanDefinition

After the ServiceRequest is created, that kicks off the process. We're working on a pub/sub workflow, but for now it we have a service that periodically polls for new ServiceRequests. It then pulls from the PlanDefinition to find what Resources need to be included in the Task. An example PlanDefinition is below:

{{< code json >}}
{
    "resourceType": "PlanDefinition",
    "description": "New Jersey Integrated Care for Kids: Screening Tools for 6-8 months",
    "name": "nat_6_8_months",
    "publisher": "MayJuun LLC",
    "status": "draft",
    "title": "New Jersey Integrated Care for Kids: Screening Tools for 6-8 months",
    "action": [
        {
        "definitionUri": "Questionnaire/f892b6b0-b908-4fc2-b73f-9890b9c1c06a",
        "participant": [
            {
            "role": {
                "coding": [
                {
                    "code": "PRN",
                    "display": "parent",
                    "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                }
                ]
            },
            "type": "related-person"
            },
            {
            "type": "patient"
            }
        ],
        "title": "First Time Demographics"
        },
        {
            "definitionUri": "Questionnaire/d2e03a84-6564-49cd-adee-fdee3b2c3f73",
            "participant": [
                {
                "role": {
                    "coding": [
                    {
                        "code": "PRN",
                        "display": "parent",
                        "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }
                    ]
                },
                "type": "related-person"
                },
                {
                "type": "patient"
                }
            ],
            "title": "Developmental Milestones: 6-8 months"
        },
        {
            "definitionUri": "Questionnaire/b2046600-e808-434a-9442-83717a088cbb",
            "participant": [
                {
                "role": {
                    "coding": [
                    {
                        "code": "PRN",
                        "display": "parent",
                        "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }
                    ]
                },
                "type": "related-person"
                },
                {
                "type": "patient"
                }
            ],
            "title": "PSC-17: Baby"
        },
        {
        "definitionUri": "Questionnaire/aa90ff2a-3db3-42e8-ab39-374df411d488",
            "participant": [
                {
                "role": {
                    "coding": [
                    {
                        "code": "PRN",
                        "display": "parent",
                        "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }
                    ]
                },
                "type": "related-person"
                },
                {
                "type": "patient"
                }
            ],
            "title": "Parent and Family Questions: 1-8 months"
        },
        {
        "definitionUri": "Questionnaire/64ce4e7c-65df-426e-9289-d96023acc315",
            "participant": [
                {
                "role": {
                    "coding": [
                    {
                        "code": "PRN",
                        "display": "parent",
                        "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }
                    ]
                },
                "type": "related-person"
                },
                {
                "type": "patient"
                }
            ],
            "title": "Emotional Changes With a New Baby"
        },
        {
        "definitionUri": "Questionnaire/77d1555a-f5b4-4caf-b3ca-69303b403336",
            "participant": [
                {
                "role": {
                    "coding": [
                    {
                        "code": "PRN",
                        "display": "parent",
                        "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }
                    ]
                },
                "type": "related-person"
                },
                {
                "type": "patient"
                }
            ],
            "title": "PEARLS Child"
        },
        {
        "definitionUri": "Questionnaire/0d6ae936-0358-4462-832f-7a46510a6dd8",
            "participant": [
                {
                "role": {
                    "coding": [
                    {
                        "code": "PRN",
                        "display": "parent",
                        "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"
                    }
                    ]
                },
                "type": "related-person"
                },
                {
                "type": "patient"
                }
            ],
            "title": "Other Questions: 1-11 months old"
        },
        {
            "definitionUri": "Measure/a1c7e19c-170c-4381-b89d-541bc04c1686",
            "title": "Score Measure for NJinCK Needs Assessment 6-8 months"
        },
        {
            "definitionUri": "ValueSet/93e22d5d-3751-4c83-b387-d824cb285e53",
            "title": "always_usually_sometimes_rarely_never"
        },
        {
            "definitionUri": "ValueSet/30015939-e327-43e6-aa86-a5ea2c3657e2",
            "title": "excellent_very_good_good_fair_poor"
        },
        {
            "definitionUri": "ValueSet/97cbfa42-d4c8-4066-b5b2-0b9e4e2f151a",
            "title": "low_medium_high_indeterminate_risk"
        },
        {
            "definitionUri": "ValueSet/895847ed-4d51-4d8f-8508-88937861d60b",
            "title": "never_sometimes_often"
        },
        {
            "definitionUri": "ValueSet/86c4b28b-9c35-4c1a-8372-4e0b0f21c286",
            "title": "not_at_all_somewhat_very_much"
        },
        {
            "definitionUri": "ValueSet/4adaf60d-2cf1-4a33-a8aa-74fb5147a50b",
            "title": "not_yet_somewhat_very_much"
        },
        {
            "definitionUri": "ValueSet/ef975cd6-a08e-48d2-b844-f7df07984ee1",
            "title": "ScoreOneIfAboveOne"
        }
    ],
    "contact": [
        {
        "name": "MayJuun LLC",
        "telecom": [
            {
            "system": "email",
            "use": "work",
            "value": "info@mayjuun.com"
            }
        ]
        }
    ],
}
{{< /code >}}

The PlanDefinitions, at least for now, are all pre-constructed, not created on the fly. We have a PlanDefinition for each age group, and as part of the actions we include all of the Questionnaires that we want the patient/parent to complete. We also include the Measure that will be used to score all of the Questionnares. Lastly, we use a number of ValueSets as the answers to the Questionnaires, and this specifies which ValueSets will be needed.

### Task

Now that we have the PlanDefinition, we can create the Task. The Task will include most of the information from the ServiceRequest and the PlanDefinition. The Task is our Questionnaire App interacts with, and it's what keeps track of the progress (you can even have sub-tasks, although we did not implement it for this workflow). An example task is below:

{{< code json >}}
{
    "resourceType": "Task",
    "status": "requested",
    "intent": "order",
    "id": "8b19a541-70a7-45dc-9bda-82194123915e",
    "priority": "routine",
    "basedOn": [
        {
            "reference": "ServiceRequest/3e452ace-12c8-40a6-b18d-28c8075deb74"
        }
    ],
    "instantiatesUri": "PlanDefinition/4840239b-4da6-4fa6-b8d6-4a1b1a7140af",
    "owner": {
        "reference": "RelatedPerson/2dceb6ad-e0be-4ca7-b622-0c57369ea5e2",
        "type": "Guarantor"
    },
    "for": {
        "reference": "Patient/66232d8f-628b-4740-b7a5-a2e736e076f5",
        "type": "Patient"
    },
    "requester": {
        "reference": "Organization/fe1318a0-a2ec-4580-9369-4949fb9ad82b"
    },
    "input": [
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/f892b6b0-b908-4fc2-b73f-9890b9c1c06a"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/4d324c81-164e-4191-ae19-c4eb2101c975"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/65c42602-98c6-44a6-9923-d27a1e54d317"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/74675baa-2481-409e-b743-aec18bcbf6ce"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/be1ccfa9-5e44-4869-8e55-7710829ad6c6"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "Measure",
                        "display": "Measure",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "Measure/fc97fd8e-ad33-477e-b33e-dc3a90fb2eb2"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/93e22d5d-3751-4c83-b387-d824cb285e53"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/30015939-e327-43e6-aa86-a5ea2c3657e2"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/97cbfa42-d4c8-4066-b5b2-0b9e4e2f151a"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/895847ed-4d51-4d8f-8508-88937861d60b"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/86c4b28b-9c35-4c1a-8372-4e0b0f21c286"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/4adaf60d-2cf1-4a33-a8aa-74fb5147a50b"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/ef975cd6-a08e-48d2-b844-f7df07984ee1"
        }
    ]
}
{{< /code >}}

As mentioned it is basically a summary of the ServiceRequest and PlanDefinition. It references both, includes the ordering Practitioner/Organization, the Owner is who is responsible to complete the questionnaires, and the "for" is the Patient. If the Patient is an adult, we still use this format to clarify that the Patient is both completing the Questionnaires and is the subject of them. It also of course includes all of the Questionnaires, Measures, and ValueSets as actions.

### Completed Task

A completed Task is an updated version of the Task above. Note, we use the ```"status"``` as ```requested```, ```in-progress```, or ```completed``` to keep track of what stage the Task is in. In addition, the completed Task now has outputs of QuestionnaireResponses and a MeasureReport:

{{< code json >}}
{
    "resourceType": "Task",
    "status": "completed",
    "intent": "order",
    "id": "8b19a541-70a7-45dc-9bda-82194123915e",
    "priority": "routine",
    "basedOn": [
        {
            "reference": "ServiceRequest/3e452ace-12c8-40a6-b18d-28c8075deb74"
        }
    ],
    "instantiatesUri": "PlanDefinition/4840239b-4da6-4fa6-b8d6-4a1b1a7140af",
    "owner": {
        "reference": "RelatedPerson/2dceb6ad-e0be-4ca7-b622-0c57369ea5e2",
        "type": "Guarantor"
    },
    "for": {
        "reference": "Patient/66232d8f-628b-4740-b7a5-a2e736e076f5",
        "type": "Patient"
    },
    "requester": {
        "reference": "Organization/fe1318a0-a2ec-4580-9369-4949fb9ad82b"
    },
    "input": [
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/f892b6b0-b908-4fc2-b73f-9890b9c1c06a"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/4d324c81-164e-4191-ae19-c4eb2101c975"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/65c42602-98c6-44a6-9923-d27a1e54d317"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/74675baa-2481-409e-b743-aec18bcbf6ce"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "questionnaire",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "Questionnaire/be1ccfa9-5e44-4869-8e55-7710829ad6c6"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "Measure",
                        "display": "Measure",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "Measure/fc97fd8e-ad33-477e-b33e-dc3a90fb2eb2"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/93e22d5d-3751-4c83-b387-d824cb285e53"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/30015939-e327-43e6-aa86-a5ea2c3657e2"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/97cbfa42-d4c8-4066-b5b2-0b9e4e2f151a"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/895847ed-4d51-4d8f-8508-88937861d60b"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/86c4b28b-9c35-4c1a-8372-4e0b0f21c286"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/4adaf60d-2cf1-4a33-a8aa-74fb5147a50b"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "ValueSet",
                        "display": "ValueSet",
                        "system": "http://hl7.org/fhir/resource-types"
                    }
                ]
            },
            "valueUri": "ValueSet/ef975cd6-a08e-48d2-b844-f7df07984ee1"
        }
    ],
    "output": [
        {
            "type": {
                "coding": [
                    {
                        "code": "collect-information",
                        "display": "Collect Information",
                        "system": "http://hl7.org/fhir/uv/cpg/CodeSystem/cpg-activity-type"
                    }
                ]
            },
            "valueUri": "QuestionnaireResponse/bc7b7824-480d-4efb-ab58-3964d9840916"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "collect-information",
                        "display": "Collect Information",
                        "system": "http://hl7.org/fhir/uv/cpg/CodeSystem/cpg-activity-type"
                    }
                ]
            },
            "valueUri": "QuestionnaireResponse/fb5d8b09-c765-4593-b01f-f0cb2e829040"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "collect-information",
                        "display": "Collect Information",
                        "system": "http://hl7.org/fhir/uv/cpg/CodeSystem/cpg-activity-type"
                    }
                ]
            },
            "valueUri": "QuestionnaireResponse/9c40b031-9252-4909-8960-1871b64f6b60"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "collect-information",
                        "display": "Collect Information",
                        "system": "http://hl7.org/fhir/uv/cpg/CodeSystem/cpg-activity-type"
                    }
                ]
            },
            "valueUri": "QuestionnaireResponse/7c37e26d-dcda-4cc2-83dc-9a601f8e427f"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "collect-information",
                        "display": "Collect Information",
                        "system": "http://hl7.org/fhir/uv/cpg/CodeSystem/cpg-activity-type"
                    }
                ]
            },
            "valueUri": "QuestionnaireResponse/15ed2cfa-4e09-4b96-90b7-004209c2a8bc"
        },
        {
            "type": {
                "coding": [
                    {
                        "code": "measureReport",
                        "system": "http://hl7.org/fhir/uv/sdc/CodeSystem/temp"
                    }
                ]
            },
            "valueUri": "MeasureReport/3a140d2a-af23-4d8d-8e50-78978f69aa23"
        }
    ]
}
{{< /code >}}

### Measure

This one was new for me. It's certainly not necessary, but I like it because it allowed me to score all of the Questionnaires in a single place. I could have created and Observation, but that would be one for each Questionnaire, and I really wanted them grouped together since the Questionnaires are being grouped together. I can't include my full fhirpath expressions because there's some proprietary information in them, but I've included enough that I think you can get the idea.

{{< code json >}}
{
  "resourceType": "Measure",
  "id": "a1c7e19c-170c-4381-b89d-541bc04c1686",
  "url": "mayjuun.com/fhir/Measure/score_nat_6_8_months",
  "name": "score_nat_6_8_months",
  "title": "Score Measure for NJinCK Needs Assessment 6-8 months",
  "status": "draft",
  "publisher": "MayJuun LLC",
  "contact": [
    {
      "name": "MayJuun LLC",
      "telecom": [
        {
          "system": "email",
          "value": "info@mayjuun.com",
          "use": "work"
        }
      ]
    }
  ],
  "description": "Scoring rubric for total and subscores for all modules for 6-8 months, along with the total Social Complexity Score",
  "scoring": {
    "coding": [
      {
        "system": "http://terminology.hl7.org/CodeSystem/measure-scoring",
        "code": "continuous-variable",
        "display": "Continuous Variable"
      }
    ]
  },
  "type": [
    {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/measure-type",
          "code": "patient-reported-outcome",
          "display": "Patient Reported Outcomes"
        }
      ]
    }
  ],
  "group": [
    {
      "description": "Scoring for Developmental Milestones: 6-8 months",
      "code": {
        "coding": [
          {
            "code": "Questionnaire/d2e03a84-6564-49cd-adee-fdee3b2c3f73"
          }
        ]
      },
      "population": [
        {
          "description": "Total Score for Developmental Milestones: 6-8 months",
          "criteria": {
            "language": "text/fhirpath",
            "expression": "entry.resource.ofType(QuestionnaireResponse).item.item.where(linkId.contains('/milestones')).answer.valueCoding.extension.value.aggregate($this + $total, 0)"
          }
        }
      ]
    },
    {
      "description": "Scoring for PSC-17: Baby",
      "code": {
        "coding": [
          {
            "code": "Questionnaire/b2046600-e808-434a-9442-83717a088cbb"
          }
        ]
      },
      "population": [
        {
          "description": "PSC-17: Baby, Irritability Subscore",
          "criteria": {
            "language": "text/fhirpath",
            "expression": "entry.resource.ofType(QuestionnaireResponse).item.item.item.where(linkId.contains('irritability')).answer.valueCoding.extension.value.aggregate($this + $total, 0)"
          }
        },
        {
          "description": "PSC-17: Baby, Total Score",
          "criteria": {
            "language": "text/fhirpath",
            "expression": "entry.resource.ofType(QuestionnaireResponse).item.item.item.where(linkId.contains('/psc_baby/')).answer.valueCoding.extension.value.aggregate($this + $total, 0)"
          }
        }
      ]
    }
  ]
}
{{< /code >}}

This one needs a little explanation. The top is obviously just the metadata, the key piece here is the group. The group is a list that I've used to contain all scores and subscores for a single questionnaire. The ```group.code.coding.code``` is the path to the Questionnaire that the scoring is applied against. I've then used the population as a list of each score or subscore that apply to a single questionnaire. For instance, the PSC-17 Baby questionnaire has both a total score and an irritability score. These are both from the same questionnaire, but different responses are used for the result. These are detailed in the FHIRPath expressions.

### MeasureReport

The MeasureReport in turn mirrors the Measure and includes the scores, along with some other pertinent information (although this will obviously vary based on your scoring and the questionnaire). An example for something like the Measure above could look like this:

{{< code json >}}
{
  "resourceType": "MeasureReport",
  "status": "complete",
  "measure": "mayjuun.com/fhir/Measure/score_nat_6_8_months",
  "subject": {
    "reference": "Patient/becebba3-813d-4585-89f9-f74c89d548fb"
  },
  "type": "individual",
  "group": [
    {
      "code": {
        "text": "Scoring for Developmental Milestones: 6-8 months"
      },
      "stratifier": [
        {
          "stratum": [
            {
              "component": [
                {
                  "code": {
                    "coding": [
                      {
                        "code": "low-risk",
                        "display": "low risk"
                      }
                    ]
                  },
                  "value": {
                    "coding": [
                      {
                        "code": "low-risk",
                        "display": "low risk",
                        "system": "mayjuun.com/fhir/ValueSet/low_medium_high_risk"
                      }
                    ]
                  }
                },
                {
                  "code": {
                    "text": "Total Score for Developmental Milestones: 23-28 months"
                  },
                  "value": {
                    "text": "Total Score for Developmental Milestones: 23-28 months"
                  }
                }
              ],
              "measureScore": {
                "value": 14
              }
            }
          ]
        }
      ]
    },
     {
      "code": {
        "text": "Scoring for PSC-17: Baby"
      },
      "stratifier": [
        {
          "stratum": [
            {
              "measureScore": {
                "value": 8
              },
              "value": {
                "text": "PSC-17: Baby, Irritability Subscore"
              }
            }
          ]
        },
        {
          "stratum": [
            {
              "component": [
                {
                  "code": {
                    "coding": [
                      {
                        "code": "At Risk",
                        "display": "At Risk"
                      }
                    ]
                  },
                  "value": {
                    "coding": [
                      {
                        "code": "high-risk",
                        "display": "high risk",
                        "system": "mayjuun.com/fhir/ValueSet/low_medium_high_risk"
                      }
                    ]
                  }
                },
                {
                  "code": {
                    "text": "PSC-17: Baby, Total Score"
                  },
                  "value": {
                    "text": "PSC-17: Baby, Total Score"
                  }
                }
              ],
              "measureScore": {
                "value": 14
              }
            }
          ]
        }
      ]
    }
  ]
}
{{< /code >}}

Aaaannnnndddd...scene. So that's our current workflow. I'm obviously open to suggestions or pointers if any of this is out of sync with what the community thinks it should be. But I wanted to offer it as an example because there are not a lot of them out there at this time.
