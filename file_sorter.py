# -*- coding: utf-8 -*-
"""File sorter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NFvX0kA_9pVdCZCJ1wF-s7c_qYGggMKT

# New Section

# New Section
"""

## Code for New Master List

import pandas as pd

#import the file
date = '(9.03 - 9.09)'

df = pd.read_excel('Class List {}.xlsx'.format(date))

# the following line of code is not to highlight the header
#pd.io.formats.excel.ExcelFormatter.header_style = None

# manupulate the data
dept_anthropology_1 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "ANTH")]

dept_architecture_2 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "ARCH")]

dept_arts_3 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                      (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                      (df['Course Campus'] == "Online & ITV")) &
                      ((df['Subject Code'] == "ARTE") |
                       (df['Subject Code'] == "ARTH") |
                       (df['Subject Code'] == "ARTS"))]

dept_bioChemistry_4 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "BIOC")]

dept_bioMedEngineering_5 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "BME")]

dept_bioMedScienceGradProgram_6 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                  (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                  (df['Course Campus'] == "Online & ITV")) &
                                  ((df['Subject Code'] == "BIOM") |
                                  (df['Subject Code'] == "MPHY"))]

dept_commAndJournalism_7 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                  (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                  (df['Course Campus'] == "Online & ITV")) &
                                  ((df['Subject Code'] == "CJ") |
                                  (df['Subject Code'] == "COMM"))]

dept_commAndRegPlanning_8 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "CRP")]

dept_earthANDPlaneteryEnvironNaturalSciences_9 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                              (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                              (df['Course Campus'] == "Online & ITV")) &
                              ((df['Subject Code'] == "EPS") |
                              (df['Subject Code'] == "ENVS") |
                              (df['Subject Code'] == "GEOL") |
                              (df['Subject Code'] == "NTSC"))]

dept_economics_10 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "ECON")]

dept_emergencyMedicalServices_11 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                        (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                        (df['Course Campus'] == "Online & ITV")) &
                                        (df['Subject Code'] == "EMS")]

dept_globalAndNationalSecurity_12 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                        (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                        (df['Course Campus'] == "Online & ITV")) &
                                        (df['Subject Code'] == "GLNS")]

dept_healthExerciseAndSportsScience_13 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                            (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                            (df['Course Campus'] == "Online & ITV")) &
                                            ((df['Subject Code'] == "ATED") |
                                            (df['Subject Code'] == "HED") |
                                            (df['Subject Code'] == "HESS") |
                                            (df['Subject Code'] == "HLED") |
                                            (df['Subject Code'] == "PENP") |
                                            (df['Subject Code'] == "PEP") |
                                            (df['Subject Code'] == "PHED") |
                                            (df['Subject Code'] == "PRPE"))]

dept_healthMedicineAndHumanValues_14 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          (df['Subject Code'] == "HMHV")]

dept_individualFamCommEducation_15 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                            (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                            (df['Course Campus'] == "Online & ITV")) &
                                            ((df['Subject Code'] == "IFCE") |
                                            (df['Subject Code'] == "COUN") |
                                            (df['Subject Code'] == "ECED") |
                                            (df['Subject Code'] == "ECME") |
                                            (df['Subject Code'] == "EDPY") |
                                            (df['Subject Code'] == "FCS")  |
                                            (df['Subject Code'] == "FCST") |
                                            (df['Subject Code'] == "NUTR"))]

dept_landscapeArchitecture_16 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          (df['Subject Code'] == "LA")]

dept_languageLiteracySocialSciences_17 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                                (df['Course Campus'] == "Online & ITV")) &
                                                (df['Subject Code'] == "LLSS")]

dept_latinAmericanStudies_18 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                      (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                      (df['Course Campus'] == "Online & ITV")) &
                                      (df['Subject Code'] == "LTAM")]

dept_mechanicalEngineering_19 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                        (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                        (df['Course Campus'] == "Online & ITV")) &
                                        (df['Subject Code'] == "ME")]

dept_museumStudies_20 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "MSST")]

dept_nanoScienceANDMicroSys_21 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          (df['Subject Code'] == "NSMS")]

dept_nursing_22 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                          (df['Course Campus'] == "Online & ITV")) &
                          ((df['Subject Code'] == "NMNC") |
                          (df['Subject Code'] == "NURS"))]

dept_organizationInformationAndLearningSciences_23 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                                            (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                                            (df['Course Campus'] == "Online & ITV")) &
                                                            ((df['Subject Code'] == "OILS") |
                                                            (df['Subject Code'] == "IADL"))]

dept_physicsAstronomy_24 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          ((df['Subject Code'] == "PHYC") |
                                          (df['Subject Code'] == "ASTR") |
                                          (df['Subject Code'] == "PHYS"))]

dept_teacherEducation_25 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          ((df['Subject Code'] == "EDUC") |
                                          (df['Subject Code'] == "LEAD") |
                                          (df['Subject Code'] == "MSET"))]

dept_universityCollegeDepartments_26 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                              (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                              (df['Course Campus'] == "Online & ITV")) &
                                              ((df['Subject Code'] == "ACAD") |
                                              (df['Subject Code'] == "CELR") |
                                              (df['Subject Code'] == "GEX") |
                                              (df['Subject Code'] == "FYEX") |
                                              (df['Subject Code'] == "LAIS") |
                                              (df['Subject Code'] == "UNIV"))]


# create the master file
df1 = pd.concat([dept_anthropology_1, dept_architecture_2, dept_arts_3, dept_bioChemistry_4, dept_bioMedEngineering_5,
                 dept_bioMedScienceGradProgram_6, dept_commAndJournalism_7, dept_commAndRegPlanning_8,
                 dept_earthANDPlaneteryEnvironNaturalSciences_9, dept_economics_10, dept_emergencyMedicalServices_11,
                 dept_globalAndNationalSecurity_12, dept_healthExerciseAndSportsScience_13, dept_healthMedicineAndHumanValues_14,
                 dept_individualFamCommEducation_15, dept_landscapeArchitecture_16, dept_languageLiteracySocialSciences_17,
                 dept_latinAmericanStudies_18, dept_mechanicalEngineering_19, dept_museumStudies_20,
                 dept_nanoScienceANDMicroSys_21, dept_nursing_22, dept_organizationInformationAndLearningSciences_23,
                 dept_physicsAstronomy_24, dept_teacherEducation_25, dept_universityCollegeDepartments_26])
df1.to_excel('Master File {}.xlsx'.format(date), index = False)



# save the output to the specified location
dept_anthropology_1.to_excel('ANTH {}.xlsx'.format(date), index = False)
dept_architecture_2.to_excel('ARCH {}.xlsx'.format(date), index = False)
dept_arts_3.to_excel('ARTE, ARTH, ARTS {}.xlsx'.format(date), index = False)
dept_bioChemistry_4.to_excel('BIOC {}.xlsx'.format(date), index = False)
dept_bioMedEngineering_5.to_excel('BME {}.xlsx'.format(date), index = False)
dept_bioMedScienceGradProgram_6.to_excel('BIOM, MPHY {}.xlsx'.format(date), index = False)
dept_commAndJournalism_7.to_excel('CJ, COMM {}.xlsx'.format(date), index = False)
dept_commAndRegPlanning_8.to_excel('CRP {}.xlsx'.format(date), index = False)
dept_earthANDPlaneteryEnvironNaturalSciences_9.to_excel('EPS, ENVS, GEOL, NTSC {}.xlsx'.format(date), index = False)
dept_economics_10.to_excel('ECON {}.xlsx'.format(date), index = False)
dept_emergencyMedicalServices_11.to_excel('EMS {} .xlsx'.format(date), index = False)
dept_globalAndNationalSecurity_12.to_excel('GLNS {}.xlsx'.format(date), index = False)
dept_healthExerciseAndSportsScience_13.to_excel('{} ATED, HED, HESS, HLED, PENP, PEP, PHED, PRPE.xlsx'.format(date), index = False)
dept_healthMedicineAndHumanValues_14.to_excel('HMHV {}.xlsx'.format(date), index = False)
dept_individualFamCommEducation_15.to_excel('{} IFCE, COUN, ECED, ECME, EDPY, FCS, FCST, NUTR.xlsx'.format(date), index = False)
dept_landscapeArchitecture_16.to_excel('LA {}.xlsx'.format(date), index = False)
dept_languageLiteracySocialSciences_17.to_excel('LLSS {}.xlsx'.format(date), index = False)
dept_latinAmericanStudies_18.to_excel('LTAM {}.xlsx'.format(date), index = False)
dept_mechanicalEngineering_19.to_excel('ME {}.xlsx'.format(date), index = False)
dept_museumStudies_20.to_excel('MSST {}.xlsx'.format(date), index = False)
dept_nanoScienceANDMicroSys_21.to_excel('NSMS {}.xlsx'.format(date), index = False)
dept_nursing_22.to_excel('NMNC, NURS {}.xlsx'.format(date), index = False)
dept_organizationInformationAndLearningSciences_23.to_excel('IADL, OILS {}.xlsx'.format(date), index = False)
dept_physicsAstronomy_24.to_excel('PHYC, ASTR, PHYS {}.xlsx'.format(date), index = False)
dept_teacherEducation_25.to_excel('EDUC, LEAD, MSET {}.xlsx'.format(date), index = False)
dept_universityCollegeDepartments_26.to_excel('{} ACAD, CELR, GEX, FYEX, LAIS, UNIV.xlsx'.format(date), index = False)

## Code for Old Master Lists

import pandas as pd

#import the file
date = '(7.9 - 7.15)'

df = pd.read_excel('Class List {}.xlsx'.format(date))

# the following line of code is not to highlight the header
#pd.io.formats.excel.ExcelFormatter.header_style = None

# manupulate the data
dept_anthropology_1 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "ANTH")]

dept_arts_2 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                      (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                      (df['Course Campus'] == "Online & ITV")) &
                      ((df['Subject Code'] == "ARTE") |
                       (df['Subject Code'] == "ARTH") |
                       (df['Subject Code'] == "ARTS"))]

dept_artsAndSciences_3 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "ARSC")]

dept_artsAndSciencesCoopWorkPhase_4 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                              (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                              (df['Course Campus'] == "Online & ITV")) &
                                              (df['Subject Code'] == "ASCP")]

dept_bioChemistry_5 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "BIOC")]

dept_commAndJournalism_6 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                  (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                  (df['Course Campus'] == "Online & ITV")) &
                                  ((df['Subject Code'] == "CJ") |
                                  (df['Subject Code'] == "COMM"))]

dept_economics_7 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "ECON")]

dept_emergencyMedicalServices_8 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                        (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                        (df['Course Campus'] == "Online & ITV")) &
                                        (df['Subject Code'] == "EMS")]

dept_engineering_9 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                            (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                            (df['Course Campus'] == "Online & ITV")) &
                            (df['Subject Code'] == "ENG")]

dept_globalAndNationalSecurity_10 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                        (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                        (df['Course Campus'] == "Online & ITV")) &
                                        (df['Subject Code'] == "GLNS")]

dept_healthExerciseAndSportsScience_11 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                            (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                            (df['Course Campus'] == "Online & ITV")) &
                                            ((df['Subject Code'] == "ATED") |
                                            (df['Subject Code'] == "HED") |
                                            (df['Subject Code'] == "HESS") |
                                            (df['Subject Code'] == "HLED") |
                                            (df['Subject Code'] == "PENP") |
                                            (df['Subject Code'] == "PEP") |
                                            (df['Subject Code'] == "PHED") |
                                            (df['Subject Code'] == "PRPE"))]

dept_healthMedicineAndHumanValues_12 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          (df['Subject Code'] == "HMHV")]

dept_individualFamCommEducation_13 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                            (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                            (df['Course Campus'] == "Online & ITV")) &
                                            ((df['Subject Code'] == "IFCE") |
                                            (df['Subject Code'] == "COUN") |
                                            (df['Subject Code'] == "ECED") |
                                            (df['Subject Code'] == "ECME") |
                                            (df['Subject Code'] == "EDPY") |
                                            (df['Subject Code'] == "FCS")  |
                                            (df['Subject Code'] == "FCST") |
                                            (df['Subject Code'] == "NUTR"))]

dept_landscapeArchitecture_14 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          (df['Subject Code'] == "LA")]

dept_languageLiteracySocialSciences_15 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                                (df['Course Campus'] == "Online & ITV")) &
                                                (df['Subject Code'] == "LLSS")]

dept_latinAmericanStudies_16 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                      (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                      (df['Course Campus'] == "Online & ITV")) &
                                      (df['Subject Code'] == "LTAM")]

dept_mechanicalEngineering_17 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                        (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                        (df['Course Campus'] == "Online & ITV")) &
                                        (df['Subject Code'] == "ME")]

dept_museumStudies_18 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                (df['Course Campus'] == "Online & ITV")) &
                                (df['Subject Code'] == "MSST")]

dept_nativeAmericanStudies_19 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          (df['Subject Code'] == "NATV")]

dept_nursing_20 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                          (df['Course Campus'] == "Online & ITV")) &
                          ((df['Subject Code'] == "NMNC") |
                          (df['Subject Code'] == "NURS"))]

dept_organizationInformationAndLearningSciences_21 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                                            (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                                            (df['Course Campus'] == "Online & ITV")) &
                                                            ((df['Subject Code'] == "OILS") |
                                                            (df['Subject Code'] == "IADL"))]

dept_radiologyNuclearMedicine_22 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          ((df['Subject Code'] == "RADS") |
                                          (df['Subject Code'] == "NUCM"))]

dept_religiousStudiesProgram_23 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          (df['Subject Code'] == "RELG")]

dept_surgeryDentalServices_24 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                        (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                        (df['Course Campus'] == "Online & ITV")) &
                                        (df['Subject Code'] == "DEHY")]

dept_teacherEducation_25 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                          (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                          (df['Course Campus'] == "Online & ITV")) &
                                          ((df['Subject Code'] == "EDUC") |
                                          (df['Subject Code'] == "LEAD") |
                                          (df['Subject Code'] == "MSET"))]

dept_universityCollegeDepartments_26 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                                              (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                                              (df['Course Campus'] == "Online & ITV")) &
                                              ((df['Subject Code'] == "ACAD") |
                                              (df['Subject Code'] == "CELR") |
                                              (df['Subject Code'] == "GEX") |
                                              (df['Subject Code'] == "FYEX") |
                                              (df['Subject Code'] == "LAIS") |
                                              (df['Subject Code'] == "UNIV"))]

dept_womenStudies_27 = df.loc[((df['Course Campus'] == "Albuquerque/Main")  |
                              (df['Course Campus'] == "Albq UNM Health Sci Rio Rancho") |
                              (df['Course Campus'] == "Online & ITV")) &
                              ((df['Subject Code'] == "GNDR") |
                              (df['Subject Code'] == "WGSS") |
                              (df['Subject Code'] == "WMST"))]


# create the master file
df1 = pd.concat([dept_anthropology_1, dept_arts_2, dept_artsAndSciences_3, dept_artsAndSciencesCoopWorkPhase_4,
                 dept_bioChemistry_5, dept_commAndJournalism_6, dept_economics_7, dept_emergencyMedicalServices_8,
                 dept_engineering_9, dept_globalAndNationalSecurity_10, dept_healthExerciseAndSportsScience_11,
                 dept_healthMedicineAndHumanValues_12, dept_individualFamCommEducation_13, dept_landscapeArchitecture_14,
                 dept_languageLiteracySocialSciences_15, dept_latinAmericanStudies_16, dept_mechanicalEngineering_17,
                 dept_museumStudies_18, dept_nativeAmericanStudies_19, dept_nursing_20, dept_organizationInformationAndLearningSciences_21,
                 dept_radiologyNuclearMedicine_22, dept_religiousStudiesProgram_23, dept_surgeryDentalServices_24,
                 dept_teacherEducation_25, dept_universityCollegeDepartments_26, dept_womenStudies_27])
df1.to_excel('Master File {}.xlsx'.format(date), index = False)



# save the output to the specified location
dept_anthropology_1.to_excel('ANTH {}.xlsx'.format(date), index = False)
dept_arts_2.to_excel('ARTE, ARTH, ARTS {}.xlsx'.format(date), index = False)
dept_artsAndSciences_3.to_excel('ARSC {}.xlsx'.format(date), index = False)
dept_artsAndSciencesCoopWorkPhase_4.to_excel('ASCP {}.xlsx'.format(date), index = False)
dept_bioChemistry_5.to_excel('BIOC {}.xlsx'.format(date), index = False)
dept_commAndJournalism_6.to_excel('CJ, COMM {}.xlsx'.format(date), index = False)
dept_economics_7.to_excel('ECON {}.xlsx'.format(date), index = False)
dept_emergencyMedicalServices_8.to_excel('EMS {}.xlsx'.format(date), index = False)
dept_engineering_9.to_excel('ENG {}.xlsx'.format(date), index = False)
dept_globalAndNationalSecurity_10.to_excel('GLNS {}.xlsx'.format(date), index = False)
dept_healthExerciseAndSportsScience_11.to_excel('{} ATED, HED, HESS, HLED, PENP, PEP, PHED, PRPE.xlsx'.format(date), index = False)
dept_healthMedicineAndHumanValues_12.to_excel('HMHV {}.xlsx'.format(date), index = False)
dept_individualFamCommEducation_13.to_excel('{} IFCE, COUN, ECED, ECME, EDPY, FCS, FCST, NUTR.xlsx'.format(date), index = False)
dept_landscapeArchitecture_14.to_excel('LA {}.xlsx'.format(date), index = False)
dept_languageLiteracySocialSciences_15.to_excel('LLSS {}.xlsx'.format(date), index = False)
dept_latinAmericanStudies_16.to_excel('LTAM {}.xlsx'.format(date), index = False)
dept_mechanicalEngineering_17.to_excel('ME {}.xlsx'.format(date), index = False)
dept_museumStudies_18.to_excel('MSST {}.xlsx'.format(date), index = False)
dept_nativeAmericanStudies_19.to_excel('NATV {}.xlsx'.format(date), index = False)
dept_nursing_20.to_excel('NMNC, NURS {}.xlsx'.format(date), index = False)
dept_organizationInformationAndLearningSciences_21.to_excel('OILS, IADL {}.xlsx'.format(date), index = False)
dept_radiologyNuclearMedicine_22.to_excel('RADS, NUCM {}.xlsx'.format(date), index = False)
dept_religiousStudiesProgram_23.to_excel('RELG {}.xlsx'.format(date), index = False)
dept_surgeryDentalServices_24.to_excel('DEHY {}.xlsx'.format(date), index = False)
dept_teacherEducation_25.to_excel('EDUC, LEAD, MSET {}.xlsx'.format(date), index = False)
dept_universityCollegeDepartments_26.to_excel('{} ACAD, CELR, GEX, FYEX, LAIS, UNIV.xlsx'.format(date), index = False)
dept_womenStudies_27.to_excel('GNDR, WGSS, WMST {}.xlsx'.format(date), index = False)





"""# New Section"""