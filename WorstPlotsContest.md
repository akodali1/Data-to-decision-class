Worst Plot Contest
================


</br>

### 1) 3D Plot of Total Count of Patients vs Program Name vs Facility

``` r
library(dplyr)
library(tidyverse)
library(plotly)
library(IRdisplay)
library(latticeExtra)
library(ggplot2)
library(gapminder)

Full_HFS_Data <- read.csv("HFS Service Data.csv")


HFS_Data <- Full_HFS_Data %>% mutate(agegroup = case_when(age >= 63  & age <= 72 ~ '63-72',
                                                     age >= 54  & age <= 63 ~ '54-63',
                                                     age >= 45  & age <= 54 ~ '45-54',
                                                     age >= 37  & age <= 45 ~ '37-45',
                                                     age >= 28  & age <= 36 ~ '28-36',
                                                     age >= 19  & age <= 27 ~ '19-27',
                                                     age >= 10  & age <= 18 ~ '10-18',
                                                     age >= 0  & age <= 8 ~ '1-9'))
worst <- as.data.frame(table(HFS_Data$program_name,HFS_Data$facility))

cloud(Freq~Var1+Var2, worst, panel.3d.cloud=panel.3dbars, col.facet=rainbow(2),
      xbase=0.4, ybase=0.4, scales=list(arrows=FALSE, col=1),
      par.settings = list(axis.line = list(col = "transparent")))
```

![](https://github.com/akodali1/Data-to-decision-class/blob/main/WorstPlotContestPlots/unnamed-chunk-1-1.png)<!-- -->

#### Reasons for the plot being bad

-   The data in the substance use column is obscured by the massive bars
    in the Mental health column which makes it difficult to view the
    plots on Substance use column.
-   The values on the z-axis are misguiding.
-   The colors are deceiving since we can mistakenly believe that the
    bars that are green are identical and vice versa.
-   Overlapping of facility names in x-axis.
-   There is no proper name formatting for z-axis heading and title
    name.

</br>

### 2) Donut Chart of visits per age group

``` r
worst1 <- as.data.frame(table(HFS_Data$agegroup))

values=c("#CC0000", "#CC1000", "#CC2000", "#CC3000", 
                             "#CC4000", "#CC5000", "#CC6000", "#CC7000")

donut <- ggplot(data = worst1, aes(x=2, y = Freq, fill = Var1))+
       geom_col(color = "black") +
       coord_polar("y", start = 0) + 
       geom_text(aes(label = paste0(round(Freq/100), "%")), 
                          position = position_stack(vjust = 0.5)) +
       theme(panel.background = element_blank(),
             axis.line = element_blank(),
             axis.text = element_blank(),
             axis.ticks = element_blank(),
             axis.title = element_blank(), 
             plot.title = element_text(hjust = 0.5, size = 18))+
       ggtitle("Donut Chart of visits per age group") +
       scale_fill_manual(values = values) +theme(legend.title = element_text("Age Groups"))+
       xlim(0.5, 2.5)

donut
```

![](WorstPlotsContest_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

#### Reasons for the plot being bad

-   In a pie chart, all of the data must add up to 100 percent, but it
    only does 86 percent in this case.
-   Matching the colors in the labels to slices is a difficult task.
-   The color of one segment is quite close to the color of the other
    segments, making it difficult to distinguish between them.
-   There is no proper labeling for the legend title.
