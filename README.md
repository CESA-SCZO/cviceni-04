# Cvičení 4

**Klonování repozitáře:**
- Klávesa Windows + R -> cmd -> Enter
```
mkdir c:\SCZO_2026
cd C:\SCZO_2026
git clone https://cesta.ke.forked.git.repozitari
uv sync
```

**Úkol 1:**
- Načtěte obraz „Matterhorn.jpg“, převeďte jej na šedotónový, vytvořte histogram obrazu
- K obrazu přičtěte hodnotu 0.3 a zobrazte jej i s odpovídajícím histogramem
- Vytvořte další obraz vynásobením původního orbazu hodnotou 1.5 a zobrazte jej i s odpovídajícím histogramem



**Úkol 2:**
- Načtěte obraz „rtg_ruka.jpg“, převeďte jej do rozsahu 0-1 a upravte jej tak, aby byla využita celá škála stupňů šedi
- Porovnejte obrazy a jejich histogramy
- Vytvořte negativ obrazu a zobrazte jej spolu s jeho histogramem
- Upravte kontrast obrazu pomocí gama transformace s hodnotou γ>1 a γ<1
- Proveďte vhodnou korekci nelineárního zkreslení v obraze „gamma.png“ pomocí gama korekce



**Úkol 3:**
- Načtěte obraz „fotbal.png“ a převeďte jej na šedotónový
- Proveďte adaptivní ekvalizaci histogramu (AHE) a zobrazte výsledný obraz s jeho histogramem
- Proveďte kontrastně omezenou ekvalizaci histogramu (CLAHE) a zobrazte výsledný obraz s jeho histogramem


**Závěr cvičení:**
```
git add .
git commit –m „message“
git push origin main
```
