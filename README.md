<p align="center">
  <img src="https://hsto.org/webt/r6/dp/ks/r6dpksrxkvmgumetfjvfjcwn4wy.png" alt="CubeCRN logo" width="400" />
</p>

<h1 align="center">cube3d.dna</h1>
 
<p align="center">
  Most advanced and compact 3d engine ever implemented in DNA code
  <br><br>
  <img alt="environment: in vitro" src="https://img.shields.io/badge/environment-in%20vitro-red"/>
  <img alt="platform: DNA | TMSD" src="https://img.shields.io/badge/platform-DNA%20%7C%20TMSD-white"/>
  <img alt="license: GPL-v.3.0+" src="https://img.shields.io/badge/license-GPL--v.3.0%2B-green.svg"/>
  <br>
  <img alt="lint status" src="https://github.com/pallada-92/dna-3d-engine/workflows/lint/badge.svg"/>
  <img alt="tests status" src="https://github.com/pallada-92/dna-3d-engine/workflows/tests/badge.svg"/>
  <img alt="coverage" src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/pallada-92/7b35716db8bedb6914c6cf2fab3a4dd0/raw/coverage_badge.json"/>
  <img alt="total lines" src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/pallada-92/7b35716db8bedb6914c6cf2fab3a4dd0/raw/loc_badge.json"/>
  <img alt="bundle size" src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/pallada-92/7b35716db8bedb6914c6cf2fab3a4dd0/raw/bundle_size_badge.json"/>  
  <!-- <img alt="active installs: 0" src="https://img.shields.io/badge/active%20installs-0-yellow"/> -->
</p>
<br />
 
## Getting started

* [Step by step tutorial](https://observablehq.com/d/45f2227392644567)
* [Try this in your browser](https://observablehq.com/d/5288cbf0a5de42b2#3d-engine)

## How to deploy

1. Synthesise oligonucleotides from [cube3d.dna](./cube3d.dna) file.
2. Arrange test tubes as shown on the diagram below.
3. Don't forget to provide initial concentrations according to the table below.
4. Use pipette to encode position (row and column) of each tube to start computation.

<details>
<summary>Environment variables</summary>

```
q = 0.01
cxtm = 0.606
axp = 0.606
cytm = 0.898
ayp = 0.898
cztm = 1.243
azp = 1.243
mxyzm = 0.3
nx = 0.036 + 0.555 Col + 0.147 Row
ny = 0.853 + -0.517 Row
nz = 0.737 + -0.270 Col + 0.302 Row
```
</details>


<p align="center">
<img src="https://habrastorage.org/webt/v8/hf/gw/v8hfgw7rpxrhw8owhwxewnalfle.png" width="600"/>
</p>

## Testing

1. Pick the fluorophore of your favourite color and attach it to the `Strand R0`, so that it activates when `R` species are being produced.
2. Use the light source of specific wavelength (depending of the fluorophore you've chosen) to render the result.

<p align="center">
<img src="https://hsto.org/webt/hv/q_/zy/hvq_zyw6uuwwfpg6umqthctq6tm.png" width="600"/>
</p>

## Ports to other languages

* [SQLite version](https://observablehq.com/@pallada-92/sql-3d-engine)
* [Excel version](https://observablehq.com/@pallada-92/excel-3d-engine-emulator)
* [JavaScript version](https://observablehq.com/d/940d2895b3e9e611)
* [Russian (Русский)](https://habr.com/ru/post/437168/)

## Gallery

<table>
  <tr>
    <td align="center" valign="center" width="50%">
      <img src="https://habrastorage.org/getpro/habr/post_images/9e2/fc9/d46/9e2fc9d4605a01c82ae317775fad1e10.gif" width="100%" /><br>
      Ray marching common implementation<br>
      <img src="https://habrastorage.org/webt/gl/b_/e8/glb_e8-jvkdoyhuri8gctsnysy4.png" width="200" />
    </td>
    <td align="center" valign="center" width="50%">
      <img src="https://habrastorage.org/webt/8n/r_/6o/8nr_6oqof2xrvhf8mbt0r4lmtmu.gif" width="100%" /><br>
      Ray marching differential form used here<br>
      <img src="https://habrastorage.org/webt/ao/ze/qh/aozeqh4htzkzvbh_po67dmh_zho.png" width="200" />
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td align="center" valign="center">
      <img src="https://habrastorage.org/webt/gw/zb/v1/gwzbv1w5humyabeelkyx_c3gq7k.gif" width="100%" /><br>
      Simplified animation of toehold mediated strand displacement technique
    </td>
    <td align="center" valign="center">
      <img src="https://habrastorage.org/webt/ph/iv/ax/phivaxoqftqzm2h7qvbbj41dwiq.png" width="100%" /><br><br>
      Types of oligonucleotides required for single reaction
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td align="center" valign="center">
      <img src="https://habrastorage.org/webt/ww/9k/xd/ww9kxd64xtigxtbpc5mm3tvsswg.png" width="100%" /><br>
      Data flow graph of JS implementation
    </td>
    <td align="center" valign="center">
      <img src="https://habrastorage.org/webt/uj/_l/2_/uj_l2_q26onfetzrpq_0wfetxic.png" width="100%" /><br>
      Species interaction graph of this implementation
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td align="center" valign="center">
      <img src="https://habrastorage.org/webt/-j/ak/5i/-jak5iv5d7pkkosrhl_g4r3oo34.png" width="100%" /><br><br>
      Unminified source code of this implementation. It is just plain reactions with a few macros.
      Minifier was written in Wolfram Language specially for this project. 
    </td>
    <td align="center" valign="center">
      <br>
      <img src="https://habrastorage.org/webt/qn/-j/bu/qn-jbugqz0opyuxhvm6j09wv5te.png" width="100%" /><br><br>
      CRN++ source code for comparison (CRN++ is not used in this implementation)
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td align="center" valign="center">
      <img src="https://habrastorage.org/webt/lv/ah/vs/lvahvszdgpw5vbvottwja7gwtjw.png" width="100%" /><br><br>
      10 reactions after minification used in this project.
      Since piperine compiler doesn't support more than 2 products in the right hand side, reactions were splitted.
    </td>
    <td align="center" valign="center">
      <br>
      <img src="https://habrastorage.org/webt/lh/hx/j8/lhhxj842nxuxdocbz1zsyazvfok.png" width="100%" /><br><br>
      CRN++ 70 reactions output for comparison (CRN++ is not used in this implementation)
    </td>
  </tr>
</table>

## Building from source

1. Install the <a href="https://github.com/DNA-and-Natural-Algorithms-Group/piperine">piperine compiler by the DNA and Natural Algorithms Group</a>.
2. Run the following command

```
piperine-design cube3d.crn --maxspurious 0.765
```

3. Wait 2-3 hours for compilation results

## References

1. David Soloveichik, Georg Seelig and Erik Winfree<br>
   <a href="https://www.pnas.org/content/107/12/5393">DNA as a universal substrate for chemical kinetics</a><br>
   Proceedings of the National Academy of Sciences Mar 2010, 107 (12) 5393-5398; DOI: 10.1073/pnas.0909380107<br><br>

1. Niranjan Srinivas, James Parkin, Georg Seelig, Erik Winfree and David Soloveichik<br>
   <a href="https://science.sciencemag.org/content/358/6369/eaal2052.full">Enzyme-free nucleic acid dynamical systems</a><br>
   Science 358, eaal2052 (2017).<br>
   Some images were taken from <a href="https://science.sciencemag.org/content/suppl/2017/12/13/358.6369.eaal2052.DC1">supplementary materials</a><br><br>

1. Chalk, Cameron, Niels Kornerup, Wyatt Reeves, and David Soloveichik.<br>
   <a href="https://arxiv.org/abs/1907.00053">Composable rate-independent computation in continuous chemical reaction networks.</a><br>
   International Conference on Computational Methods in Systems Biology, pp. 256-273. Springer, Cham, 2018.<br><br>

1. Chen, Ho-Lin, David Doty, and David Soloveichik.<br>
   <a href="https://dl.acm.org/doi/abs/10.1145/2554797.2554827">Rate-independent computation in continuous chemical reaction networks.</a><br>
   Proceedings of the 5th conference on Innovations in theoretical computer science. 2014.<br><br>

1. Marko Vasic, David Soloveichik and Sarfraz Khurshid<br>
   <a href="https://arxiv.org/abs/1809.07430">CRN++: Molecular Programming Language</a><br>
   Natural Computing (2020) 19:391–407 DOI: 10.1007/s11047-019-09775-1<br><br>

1. Inigo Quilez<br>
   https://www.iquilezles.org/www/index.htm<br>
   Introduction to Raymarching Signed Distance Functions
