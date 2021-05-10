# Diplomová práca: Experimentálny rozpoznávač spontánnej reči

## Popis práce
V tejto práci sa zameriavame na vytvorenie experimentálneho rozpoznávaču spontánnej reči v spolupráci s Transparency International Slovensko (TISK). Vytváraný rozpoznávač má byť využitý na prepis zvukových nahrávok do textovej podoby. Po analýze možností riešenia sme sa rozhodli pre dosiahnutie nášho cieľa využiť open-source nástroj Kaldi, ktorý je zameraný na automatické rozpoznávanie reči a vo svojom jadre využíva skryté markovovské modely (HMM) a hlboké neurónové siete (DNN).

V prvej fáze práce sme sa zamerali predovšetkým na špecifikáciu zadania a analýzu domény. Cieľom bolo oboznámiť s problematikou automatického rozpoznávania reči a základnými konceptami. Súšasne sme vykonávali aj analýzu dostupných nástrojov na spracovanie reči, po ktorej sme sa rozhodli pre použitie nástroju Kaldi. Nakoľko sme s týmto nástrojom nemali predchádzajúce skúsenosti, tak sme sa v ďalšej fáze zamerali na oboznámenie sa s ním. Po získaní nahrávok, ich prepisov od TISK sme sa rozhodli pre vykonanie prvého experimentu, vďaka ktorému sme prenikli do hĺbky nástroju Kaldi a získali tak množstvo cenných informácii, ktoré zúžitkujeme v ďalších fázach práce.

V nasledujúcich častiach uvádzame zadefinované ciele pre predošlé a nasledujúce obdobia ako aj ich plnenie.

## Ciele práce LS 2021

 - [x] Hĺbkové oboznámenie sa s témou práce a analýza domény
 - [x] Analýza open-source ASR toolkitov
 - [x] Získanie a spracovanie nahrávok v spolupráci s TISK
 - [x] Oboznámenie sa s nástrojom Kaldi
 - [x] Vykonanie prvého experimentu v nástroji Kaldi
 - [x] Vytvorenie dokumentácie v Latex-u a spísanie pokroku

## Ciele práce ZS 2021
- [ ] Dopísanie teoretickej časti diplomovej práce
- [ ] Preskúmanie možností využitia DNN (deep neural networks)
- [ ] Vykonanie druhého experimentu v nástroji Kaldi (s použitím DNN)
- [ ] Akvizícia zvukových dát a prepisov
- ... ďalšie ciele budú upresnené po konzultácii so školiteľom

## Ciele práce ZS 2021
- [ ] Plánované odovzdanie práce (Máj 2022)
- ... ďalšie ciele budú upresnené po konzultácii so školiteľom

## Obsah repozitáru
- **Diplomovka_Andrej_Kapusta.pdf** - PDF dokument diplomovej práce
- **Experimenty** - priečinok, ktorý obsahuje archívy čiastočných Kaldi projektov, ktoré boli súčasťou rôznych experimentov
- **Utility** - priečinok, ktorý obsahuje pomocné programy a skripty použité pri experimentoch
