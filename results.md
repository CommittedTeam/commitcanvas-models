## Tools and packages used for these outputs

### Mann–Whitney U statistical test results

https://pingouin-stats.org/generated/pingouin.mwu.html

### Boxplots

[seaborn](https://seaborn.pydata.org/generated/seaborn.boxplot.html) for creating plots

[boxplot_stats](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats) for getting the dictionaries of statistics used to draw a series of box and whisker plots.

## Cross project

### Mann–Whitney U statistical test results
- cross project vs project split 80/20

```

 Result for precision
      U-val       tail     p-val       RBC      CLES
MWU  1035.0  two-sided  0.009337  0.290123  0.354938

 Result for recall
     U-val       tail     p-val       RBC      CLES
MWU  910.0  two-sided  0.000758  0.375857  0.312071

 Result for fscore
     U-val       tail     p-val       RBC      CLES
MWU  997.5  two-sided  0.004656  0.315844  0.342078

```

- cross project vs project split 75/25

```

 Result for precision
      U-val       tail     p-val       RBC      CLES
MWU  1184.5  two-sided  0.093004  0.187586  0.406207

 Result for recall
     U-val       tail     p-val       RBC      CLES
MWU  976.5  two-sided  0.003087  0.330247  0.334877

 Result for fscore
      U-val       tail     p-val       RBC      CLES
MWU  1098.0  two-sided  0.026995  0.246914  0.376543


```

- cross project vs project split 60/40

```
 Result for precision
      U-val       tail     p-val       RBC      CLES
MWU  1368.0  two-sided  0.581903  0.061728  0.469136

 Result for recall
      U-val       tail     p-val       RBC      CLES
MWU  1119.5  two-sided  0.037601  0.232167  0.383916

 Result for fscore
      U-val       tail     p-val       RBC      CLES
MWU  1230.0  two-sided  0.161716  0.156379  0.421811

```

### Boxplot stats

![cross_project](commitcanvas_models/classification_reports/boxplots/cross_project.png)

```

Overall boxplot stats for precision
[{'mean': 0.6648148148148147, 'iqr': 0.08750000000000002, 'cilo': 0.6413056303658423, 'cihi': 0.6786943696341577, 'whishi': 0.79, 'whislo': 0.55, 'fliers': array([], dtype=float64), 'q1': 0.62, 'med': 0.66, 'q3': 0.7075}]

Project at the value of mean
                       name  precision  recall  fscore   fix  docs  feat  chore  refactor  test
16  material-components-web       0.66    0.65    0.65   912   649   690    692       212   150
21              angular-cli       0.66    0.62    0.62  2133   498   906    359       773   508
32                  vue-cli       0.66    0.65    0.64   950   381   478    553       135   143
41         electron-builder       0.66    0.62    0.63   872   173   567    151        98    74

Project at the value of whishi
      name  precision  recall  fscore  fix  docs  feat  chore  refactor  test
18  RSSHub       0.79    0.75    0.76  907   376  1398     94        50    79

Project at the value of whislo
       name  precision  recall  fscore  fix  docs  feat  chore  refactor  test
2  element3       0.55    0.47    0.45  337   195    57    387       244    98



Overall boxplot stats for recall
[{'mean': 0.6188888888888889, 'iqr': 0.10750000000000004, 'cilo': 0.5970326315923205, 'cihi': 0.6429673684076795, 'whishi': 0.75, 'whislo': 0.45, 'fliers': array([], dtype=float64), 'q1': 0.5725, 'med': 0.62, 'q3': 0.68}]

Project at the value of mean
                name  precision  recall  fscore   fix  docs  feat  chore  refactor  test
1    ionic-framework       0.65    0.62    0.61  2820  1300   716   1759       665   520
19     loopback-next       0.71    0.62    0.65   764   513   831   2540       144   104
21       angular-cli       0.66    0.62    0.62  2133   498   906    359       773   508
38                G2       0.65    0.62    0.62   743    94   494    461       143   110
41  electron-builder       0.66    0.62    0.63   872   173   567    151        98    74
45             lerna       0.61    0.62    0.60   356    86   265    441       177   125

Project at the value of whishi
      name  precision  recall  fscore  fix  docs  feat  chore  refactor  test
18  RSSHub       0.79    0.75    0.76  907   376  1398     94        50    79

Project at the value of whislo
                  name  precision  recall  fscore   fix  docs  feat  chore  refactor  test
40  super-productivity       0.71    0.45    0.44  1206    99  3393    391       626   101



Overall boxplot stats for fscore
[{'mean': 0.6142592592592593, 'iqr': 0.09000000000000008, 'cilo': 0.595771505519152, 'cihi': 0.634228494480848, 'whishi': 0.76, 'whislo': 0.44, 'fliers': array([], dtype=float64), 'q1': 0.57, 'med': 0.615, 'q3': 0.66}]

Project at the value of mean
                name  precision  recall  fscore   fix  docs  feat  chore  refactor  test
1    ionic-framework       0.65    0.62    0.61  2820  1300   716   1759       665   520
10  instantsearch.js       0.65    0.61    0.61   606   380   433    804        65    95
44           stryker       0.62    0.61    0.61   261   102   330    228        91   116
53              taro       0.62    0.61    0.61  2611   479  1253    997       308   129

Project at the value of whishi
      name  precision  recall  fscore  fix  docs  feat  chore  refactor  test
18  RSSHub       0.79    0.75    0.76  907   376  1398     94        50    79

Project at the value of whislo
                  name  precision  recall  fscore   fix  docs  feat  chore  refactor  test
40  super-productivity       0.71    0.45    0.44  1206    99  3393    391       626   101

```
## Project

### Mann–Whitney U statistical test results

- project 80/20 vs project 75/25

```

 Result for precision
      U-val       tail     p-val       RBC      CLES
MWU  1590.0  two-sided  0.418529 -0.090535  0.545267

 Result for recall
      U-val       tail     p-val       RBC      CLES
MWU  1512.0  two-sided  0.742015 -0.037037  0.518519

 Result for fscore
      U-val       tail     p-val       RBC      CLES
MWU  1541.0  two-sided  0.611725 -0.056927  0.528464

```

- project 80/20 vs project 60/40

```

 Result for precision
      U-val       tail     p-val      RBC      CLES
MWU  1756.0  two-sided  0.067238 -0.20439  0.602195

 Result for recall
      U-val       tail     p-val       RBC      CLES
MWU  1656.0  two-sided  0.224463 -0.135802  0.567901

 Result for fscore
      U-val       tail     p-val       RBC     CLES
MWU  1689.5  two-sided  0.155415 -0.158779  0.57939

```

- project 75/25 vs 60/40

```

 Result for precision
      U-val       tail    p-val       RBC      CLES
MWU  1621.0  two-sided  0.31744 -0.111797  0.555898

 Result for recall
      U-val       tail     p-val       RBC      CLES
MWU  1593.0  two-sided  0.408078 -0.092593  0.546296

 Result for fscore
      U-val       tail     p-val       RBC      CLES
MWU  1590.5  two-sided  0.416969 -0.090878  0.545439

```

### Boxplot stats

- 80/20

![project_80_20](commitcanvas_models/classification_reports/boxplots/project_80_20.png)

```

Overall boxplot stats for precision
[{'mean': 0.6968518518518519, 'iqr': 0.07999999999999996, 'cilo': 0.6779080049059129, 'cihi': 0.712091995094087, 'whishi': 0.85, 'whislo': 0.54, 'fliers': array([0.49, 0.52]), 'q1': 0.66, 'med': 0.695, 'q3': 0.74}]

Project at the value of mean
         name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
35  webiny-js        0.7    0.71    0.69  ...        273       812             58         90
53       taro        0.7    0.63    0.65  ...        147       634             51         11

[2 rows x 22 columns]

Project at the value of whishi
             name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
19  loopback-next       0.85    0.85    0.84  ...        103        94              9         11

[1 rows x 22 columns]

Project at the value of whislo
       name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
2  element3       0.54    0.52     0.5  ...          8        60             93         24

[1 rows x 22 columns]

Far outlier projects
         name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
37  chakra-ui       0.49    0.51    0.46  ...        120       182             33         14
44    stryker       0.52    0.54    0.51  ...         68        56             18         22

[2 rows x 22 columns]



Overall boxplot stats for recall
[{'mean': 0.6725925925925925, 'iqr': 0.08999999999999997, 'cilo': 0.6507715055191521, 'cihi': 0.689228494480848, 'whishi': 0.85, 'whislo': 0.51, 'fliers': array([0.48]), 'q1': 0.63, 'med': 0.67, 'q3': 0.72}]

Project at the value of mean
                name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
0          sequelize       0.67    0.67    0.64  ...         22       116             41         23
10  instantsearch.js       0.63    0.67    0.65  ...        137       134             26         19
15    vue-test-utils       0.74    0.67    0.68  ...         23        46              4          7

[3 rows x 22 columns]

Project at the value of whishi
             name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
19  loopback-next       0.85    0.85    0.84  ...        103        94              9         11

[1 rows x 22 columns]

Project at the value of whislo
         name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
37  chakra-ui       0.49    0.51    0.46  ...        120       182             33         14

[1 rows x 22 columns]

Far outlier projects
            name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
23  ng-bootstrap       0.67    0.48    0.47  ...         55        94             19         58

[1 rows x 22 columns]



Overall boxplot stats for fscore
[{'mean': 0.6594444444444443, 'iqr': 0.09749999999999992, 'cilo': 0.6291691309790814, 'cihi': 0.6708308690209186, 'whishi': 0.84, 'whislo': 0.47, 'fliers': array([0.46]), 'q1': 0.6125, 'med': 0.65, 'q3': 0.71}]

Project at the value of mean
        name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
8    rest.js       0.68    0.64    0.66  ...         35        48             12         39
20  renovate       0.69    0.68    0.66  ...        290       517            247         27

[2 rows x 22 columns]

Project at the value of whishi
             name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
19  loopback-next       0.85    0.85    0.84  ...        103        94              9         11

[1 rows x 22 columns]

Project at the value of whislo
            name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
23  ng-bootstrap       0.67    0.48    0.47  ...         55        94             19         58

[1 rows x 22 columns]

Far outlier projects
         name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
37  chakra-ui       0.49    0.51    0.46  ...        120       182             33         14

[1 rows x 22 columns]

```

- 75/25

![project_75_25](commitcanvas_models/classification_reports/boxplots/project_75_25.png)

```

Overall boxplot stats for precision
[{'mean': 0.6872222222222221, 'iqr': 0.09999999999999998, 'cilo': 0.6636350061323912, 'cihi': 0.7063649938676089, 'whishi': 0.85, 'whislo': 0.54, 'fliers': array([0.47]), 'q1': 0.64, 'med': 0.685, 'q3': 0.74}]

Project at the value of mean
                    name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
8                rest.js       0.69    0.62    0.65  ...         37        52             15         43
9                 gatsby       0.69    0.67    0.67  ...        229       715             35         20
26  camunda-bpm-platform       0.69    0.67    0.68  ...        501       608              9        134
45                 lerna       0.69    0.67    0.65  ...         99        57             45         38

[4 rows x 22 columns]

Project at the value of whishi
             name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
19  loopback-next       0.85    0.84    0.83  ...        138       129             10         20

[1 rows x 22 columns]

Project at the value of whislo
       name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
44  stryker       0.54    0.54     0.5  ...         84        62             22         36

[1 rows x 22 columns]

Far outlier projects
                       name  precision  recall  ...  fix_test  refactor_test  test_test
16  material-components-web       0.47    0.53  ...       229            124         28

[1 rows x 22 columns]



Overall boxplot stats for recall
[{'mean': 0.6677777777777778, 'iqr': 0.08999999999999997, 'cilo': 0.6507715055191521, 'cihi': 0.689228494480848, 'whishi': 0.84, 'whislo': 0.5, 'fliers': array([0.48]), 'q1': 0.62, 'med': 0.67, 'q3': 0.71}]

Project at the value of mean
                    name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
3                   vite       0.67    0.67    0.66  ...         50       218             25         11
9                 gatsby       0.69    0.67    0.67  ...        229       715             35         20
26  camunda-bpm-platform       0.69    0.67    0.68  ...        501       608              9        134
45                 lerna       0.69    0.67    0.65  ...         99        57             45         38

[4 rows x 22 columns]

Project at the value of whishi
             name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
19  loopback-next       0.85    0.84    0.83  ...        138       129             10         20

[1 rows x 22 columns]

Project at the value of whislo
         name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
37  chakra-ui       0.57     0.5    0.46  ...        135       230             39         22

[1 rows x 22 columns]

Far outlier projects
            name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
23  ng-bootstrap       0.63    0.48    0.45  ...         64       112             26         64

[1 rows x 22 columns]



Overall boxplot stats for fscore
[{'mean': 0.6516666666666666, 'iqr': 0.11499999999999999, 'cilo': 0.6254302570522499, 'cihi': 0.6745697429477502, 'whishi': 0.83, 'whislo': 0.45, 'fliers': array([], dtype=float64), 'q1': 0.5925, 'med': 0.65, 'q3': 0.7075}]

Project at the value of mean
                  name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
8              rest.js       0.69    0.62    0.65  ...         37        52             15         43
40  super-productivity       0.64    0.68    0.65  ...        752       313            172         92
45               lerna       0.69    0.67    0.65  ...         99        57             45         38
51                jina       0.67    0.65    0.65  ...        120       207            115         84

[4 rows x 22 columns]

Project at the value of whishi
             name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
19  loopback-next       0.85    0.84    0.83  ...        138       129             10         20

[1 rows x 22 columns]

Project at the value of whislo
            name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
23  ng-bootstrap       0.63    0.48    0.45  ...         64       112             26         64

[1 rows x 22 columns]

```

- 60/40

![project_60_40](commitcanvas_models/classification_reports/boxplots/project_60_40.png)

```

Overall boxplot stats for precision
[{'mean': 0.6718518518518517, 'iqr': 0.09999999999999998, 'cilo': 0.6436350061323912, 'cihi': 0.6863649938676089, 'whishi': 0.83, 'whislo': 0.51, 'fliers': array([0.48]), 'q1': 0.63, 'med': 0.665, 'q3': 0.73}]

Project at the value of mean
                  name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
8              rest.js       0.67    0.53    0.57  ...         57        78             29         74
22                deno       0.67    0.64    0.62  ...        131       287            120         26
40  super-productivity       0.67    0.70    0.68  ...       1306       479            285         92

[3 rows x 22 columns]

Project at the value of whishi
      name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
18  RSSHub       0.83    0.82    0.81  ...        644       392              5          7

[1 rows x 22 columns]

Project at the value of whislo
       name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
44  stryker       0.51    0.51    0.47  ...        131        90             35         60

[1 rows x 22 columns]

Far outlier projects
        name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
47  superset       0.48    0.55    0.47  ...        182       327             54         91

[1 rows x 22 columns]



Overall boxplot stats for recall
[{'mean': 0.6533333333333334, 'iqr': 0.09999999999999998, 'cilo': 0.6286350061323912, 'cihi': 0.6713649938676088, 'whishi': 0.82, 'whislo': 0.5, 'fliers': array([], dtype=float64), 'q1': 0.61, 'med': 0.65, 'q3': 0.71}]

Project at the value of mean
                name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
0          sequelize       0.66    0.65    0.64  ...         51       242             59         28
41  electron-builder       0.64    0.65    0.62  ...        189       400             23         18

[2 rows x 22 columns]

Project at the value of whishi
      name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
18  RSSHub       0.83    0.82    0.81  ...        644       392              5          7

[1 rows x 22 columns]

Project at the value of whislo
         name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
34  verdaccio       0.57     0.5     0.5  ...         82       111             67         26

[1 rows x 22 columns]



Overall boxplot stats for fscore
[{'mean': 0.6362962962962961, 'iqr': 0.11749999999999994, 'cilo': 0.6048961322055596, 'cihi': 0.6551038677944404, 'whishi': 0.81, 'whislo': 0.45, 'fliers': array([], dtype=float64), 'q1': 0.5825, 'med': 0.63, 'q3': 0.7}]

Project at the value of mean
        name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
0  sequelize       0.66    0.65    0.64  ...         51       242             59         28

[1 rows x 22 columns]

Project at the value of whishi
      name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
18  RSSHub       0.83    0.82    0.81  ...        644       392              5          7

[1 rows x 22 columns]

Project at the value of whislo
            name  precision  recall  fscore  ...  feat_test  fix_test  refactor_test  test_test
23  ng-bootstrap       0.64    0.51    0.45  ...        110       183             44         85

[1 rows x 22 columns]

```