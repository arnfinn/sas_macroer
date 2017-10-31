Dokumentasjon av SAS-makroene.

Makroene ligger her:
```
\\tos-sas-skde-01\SKDE_SAS\Makroer\master
```
For å bruke de i din egen SAS-kode, legges følgende inn i koden:
```
%let filbane=\\tos-sas-skde-01\SKDE_SAS\;
options sasautos=("&filbane.Makroer\master" SASAUTOS);
```

Hvis man vil lage en ny makro, lager man en sas-fil som heter det samme som makroen. Makroene dokumenteres direkte i koden. Eksempel på makro, som legges i en fil som heter `minNyeMakro.sas`:
```
%macro minNyeMakro(variabel1 = );

/*!
Min dokumentasjon av makroen minNyeMakro
*/

sas-kode...

%mend;
```



Alt som ligger mellom `/*!` og `*/` vil legges inn i `docs/minNyeMakro.md` av scriptet `lagDokumentasjon.py`. Ved å kjøre dette scriptet og så dytte opp til *github*, vil dokumentasjon legges på nett.

## Linker til dokumentasjon av de ulike makroene
- [Episode_of_care](Episode_of_care)
- [Episode_of_care_test](Episode_of_care_test)
- [ForholdsMatrise](ForholdsMatrise)
- [Hyppigste](Hyppigste)
- [Hyppigste_petter](Hyppigste_petter)
- [Label_m_info](Label_m_info)
- [Multippel_test](Multippel_test)
- [Unik_pasient](Unik_pasient)
- [UnikeVariableAvdOpphold](UnikeVariableAvdOpphold)
- [VarFraParvus](VarFraParvus)
- [VarFraParvusT17](VarFraParvusT17)
- [boomraader](boomraader)
- [reinnleggelser](reinnleggelser)
- [reinnleggelser_test](reinnleggelser_test)
- [test_makroer](test_makroer)
- [type1_type2_bohf](type1_type2_bohf)
