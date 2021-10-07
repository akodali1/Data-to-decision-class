# DATA EXPLORATION ON HFS SERVICE DATA

<br>

### Reading the HFS Service Data and obtaining the head of it.

    library(ggplot2)
    serdat <- read.csv("HFS Service Data.csv")
    head(serdat,20)

    ##    gender  program_name              program_type
    ## 1    Male Mental Health Counseling and Prevention
    ## 2  Female Mental Health Counseling and Prevention
    ## 3  Female Mental Health Counseling and Prevention
    ## 4  Female Mental Health Counseling and Prevention
    ## 5  Female Mental Health Counseling and Prevention
    ## 6  Female Mental Health Counseling and Prevention
    ## 7  Female Mental Health Counseling and Prevention
    ## 8  Female Mental Health Counseling and Prevention
    ## 9  Female Mental Health Counseling and Prevention
    ## 10 Female Mental Health Counseling and Prevention
    ## 11 Female Mental Health Counseling and Prevention
    ## 12 Female Mental Health Counseling and Prevention
    ## 13 Female Mental Health Counseling and Prevention
    ## 14 Female Mental Health Counseling and Prevention
    ## 15 Female Mental Health Counseling and Prevention
    ## 16 Female Mental Health Counseling and Prevention
    ## 17 Female Mental Health Counseling and Prevention
    ## 18 Female Mental Health Counseling and Prevention
    ## 19 Female Mental Health Counseling and Prevention
    ## 20 Female Mental Health Counseling and Prevention
    ##                            facility           job_title       staff_name
    ## 1  Heartland Family Service - Logan Clinical Supervisor   Poore, Lindsay
    ## 2                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 3                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 4                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 5                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 6                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 7                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 8                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 9                Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 10               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 11               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 12               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 13               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 14               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 15               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 16               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 17               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 18               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 19               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ## 20               Center Mall Office        THERAPIST II Carlson, Kaitlin
    ##    actual_date duration                     event_name activity_type
    ## 1          961     0:00 Daily Living Assessment DLA 20              
    ## 2          857     0:02                Collateral Note         Phone
    ## 3          682     0:51             Individual Therapy              
    ## 4          710     0:00             Individual Therapy              
    ## 5          696     0:50             Individual Therapy              
    ## 6          772     1:20           Case Management Note              
    ## 7          794     0:04                Collateral Note         Phone
    ## 8          864     0:02                Collateral Note  Text Message
    ## 9          661     0:52             Individual Therapy              
    ## 10         737     1:55           Case Management Note              
    ## 11         702     0:00 Daily Living Assessment DLA 20              
    ## 12         689     0:51             Individual Therapy              
    ## 13         780     0:00             Individual Therapy              
    ## 14         653     0:03                Collateral Note         Phone
    ## 15         815     0:50           Case Management Note              
    ## 16         675     0:51             Individual Therapy              
    ## 17         731     0:02                Collateral Note         Phone
    ## 18         808     0:50             Individual Therapy              
    ## 19         829     0:02                Collateral Note         Phone
    ## 20         731     0:00             Individual Therapy              
    ##    encounter_with is_client_involved is_noshow is_locked is_billed is_paid
    ## 1                               TRUE     FALSE     FALSE     FALSE   FALSE
    ## 2          Client               TRUE     FALSE      TRUE     FALSE   FALSE
    ## 3                               TRUE     FALSE      TRUE      TRUE   FALSE
    ## 4                               TRUE      TRUE      TRUE     FALSE   FALSE
    ## 5                               TRUE     FALSE      TRUE      TRUE   FALSE
    ## 6                               TRUE     FALSE      TRUE     FALSE   FALSE
    ## 7          Client               TRUE     FALSE      TRUE     FALSE   FALSE
    ## 8          Client               TRUE     FALSE      TRUE     FALSE   FALSE
    ## 9                               TRUE     FALSE      TRUE      TRUE   FALSE
    ## 10                              TRUE     FALSE      TRUE     FALSE   FALSE
    ## 11                              TRUE     FALSE      TRUE     FALSE   FALSE
    ## 12                              TRUE     FALSE      TRUE      TRUE   FALSE
    ## 13                              TRUE      TRUE      TRUE     FALSE   FALSE
    ## 14         Client               TRUE     FALSE      TRUE     FALSE   FALSE
    ## 15                              TRUE     FALSE      TRUE     FALSE   FALSE
    ## 16                              TRUE     FALSE      TRUE      TRUE   FALSE
    ## 17         Client               TRUE     FALSE      TRUE     FALSE   FALSE
    ## 18                              TRUE     FALSE      TRUE      TRUE   FALSE
    ## 19         Client               TRUE     FALSE      TRUE     FALSE   FALSE
    ## 20                              TRUE      TRUE      TRUE     FALSE   FALSE
    ##    date_entered   user_entered_name approved_date approved_staff_name submitted
    ## 1           961      Poore, Lindsay            NA                              
    ## 2           857 Carlson, Kaitlin V.           857 Carlson, Kaitlin V.  Approved
    ## 3           683 Carlson, Kaitlin V.           689        Stanek, Sean  Approved
    ## 4           710 Carlson, Kaitlin V.           714        Stanek, Sean  Approved
    ## 5           696 Carlson, Kaitlin V.           697        Stanek, Sean  Approved
    ## 6           773 Carlson, Kaitlin V.           773        Stanek, Sean  Approved
    ## 7           795 Carlson, Kaitlin V.           795 Carlson, Kaitlin V.  Approved
    ## 8           864 Carlson, Kaitlin V.           864 Carlson, Kaitlin V.  Approved
    ## 9           661 Carlson, Kaitlin V.           662        Stanek, Sean  Approved
    ## 10          739 Carlson, Kaitlin V.           739        Stanek, Sean  Approved
    ## 11          702 Carlson, Kaitlin V.           702 Carlson, Kaitlin V.  Approved
    ## 12          690 Carlson, Kaitlin V.           690        Stanek, Sean  Approved
    ## 13          780 Carlson, Kaitlin V.           781        Stanek, Sean  Approved
    ## 14          654 Carlson, Kaitlin V.           654 Carlson, Kaitlin V.  Approved
    ## 15          815 Carlson, Kaitlin V.           820 Carlson, Kaitlin V.  Approved
    ## 16          676 Carlson, Kaitlin V.           676        Stanek, Sean  Approved
    ## 17          731 Carlson, Kaitlin V.           731 Carlson, Kaitlin V.  Approved
    ## 18          808 Carlson, Kaitlin V.           820 Carlson, Kaitlin V.  Approved
    ## 19          829 Carlson, Kaitlin V.           829 Carlson, Kaitlin V.  Approved
    ## 20          731 Carlson, Kaitlin V.           731        Stanek, Sean  Approved
    ##    is_approved is_notapproved is_notapproved_subm
    ## 1            0              0                   1
    ## 2            1              0                   0
    ## 3            1              0                   0
    ## 4            1              0                   0
    ## 5            1              0                   0
    ## 6            1              0                   0
    ## 7            1              0                   0
    ## 8            1              0                   0
    ## 9            1              0                   0
    ## 10           1              0                   0
    ## 11           1              0                   0
    ## 12           1              0                   0
    ## 13           1              0                   0
    ## 14           1              0                   0
    ## 15           1              0                   0
    ## 16           1              0                   0
    ## 17           1              0                   0
    ## 18           1              0                   0
    ## 19           1              0                   0
    ## 20           1              0                   0
    ##                 program_unit_description sc_code duration_num do_not_bill
    ## 1  Behavioral Health IA -  Mental Health 1311-16            0       FALSE
    ## 2   Behavioral Health NE - Mental Health 1311-05            2       FALSE
    ## 3   Behavioral Health NE - Mental Health 1311-05           51       FALSE
    ## 4   Behavioral Health NE - Mental Health 1311-05            0       FALSE
    ## 5   Behavioral Health NE - Mental Health 1311-05           50       FALSE
    ## 6   Behavioral Health NE - Mental Health 1311-05           80       FALSE
    ## 7   Behavioral Health NE - Mental Health 1311-05            4       FALSE
    ## 8   Behavioral Health NE - Mental Health 1311-05            2       FALSE
    ## 9   Behavioral Health NE - Mental Health 1311-05           52       FALSE
    ## 10  Behavioral Health NE - Mental Health 1311-05          115       FALSE
    ## 11  Behavioral Health NE - Mental Health 1311-05            0       FALSE
    ## 12  Behavioral Health NE - Mental Health 1311-05           51       FALSE
    ## 13  Behavioral Health NE - Mental Health 1311-05            0       FALSE
    ## 14  Behavioral Health NE - Mental Health 1311-05            3       FALSE
    ## 15  Behavioral Health NE - Mental Health 1311-05           50       FALSE
    ## 16  Behavioral Health NE - Mental Health 1311-05           51       FALSE
    ## 17  Behavioral Health NE - Mental Health 1311-05            2       FALSE
    ## 18  Behavioral Health NE - Mental Health 1311-05           50       FALSE
    ## 19  Behavioral Health NE - Mental Health 1311-05            2       FALSE
    ## 20  Behavioral Health NE - Mental Health 1311-05            0       FALSE
    ##    do_not_pay   general_location             program_modifier
    ## 1       FALSE                                No Modifier - IA
    ## 2       FALSE   Homeless Shelter Heartland Housing Navigation
    ## 3       FALSE               Home Heartland Housing Navigation
    ## 4       FALSE Telehealth - Phone Heartland Housing Navigation
    ## 5       FALSE Telehealth - Phone Heartland Housing Navigation
    ## 6       FALSE               Home Heartland Housing Navigation
    ## 7       FALSE   Homeless Shelter Heartland Housing Navigation
    ## 8       FALSE                    Heartland Housing Navigation
    ## 9       FALSE Telehealth - Phone Heartland Housing Navigation
    ## 10      FALSE               Home Heartland Housing Navigation
    ## 11      FALSE                    Heartland Housing Navigation
    ## 12      FALSE               Home Heartland Housing Navigation
    ## 13      FALSE               Home Heartland Housing Navigation
    ## 14      FALSE               Home Heartland Housing Navigation
    ## 15      FALSE   Homeless Shelter Heartland Housing Navigation
    ## 16      FALSE Telehealth - Phone Heartland Housing Navigation
    ## 17      FALSE Telehealth - Phone Heartland Housing Navigation
    ## 18      FALSE   Homeless Shelter Heartland Housing Navigation
    ## 19      FALSE   Homeless Shelter Heartland Housing Navigation
    ## 20      FALSE               Home Heartland Housing Navigation
    ##    program_modifier_code NormalWorkHours duration_other_num duration_other
    ## 1                  NMODI             Yes                  0           0:00
    ## 2                    HHN             Yes                  0           0:00
    ## 3                    HHN             Yes                 10           0:10
    ## 4                    HHN             Yes                  0           0:00
    ## 5                    HHN             Yes                 10           0:10
    ## 6                    HHN             Yes                 10           0:10
    ## 7                    HHN             Yes                  0           0:00
    ## 8                    HHN             Yes                  0           0:00
    ## 9                    HHN             Yes                 10           0:10
    ## 10                   HHN             Yes                 10           0:10
    ## 11                   HHN             Yes                  0           0:00
    ## 12                   HHN             Yes                 10           0:10
    ## 13                   HHN             Yes                  0           0:00
    ## 14                   HHN             Yes                  0           0:00
    ## 15                   HHN             Yes                 10           0:10
    ## 16                   HHN             Yes                 10           0:10
    ## 17                   HHN             Yes                  0           0:00
    ## 18                   HHN             Yes                 10           0:10
    ## 19                   HHN             Yes                  0           0:00
    ## 20                   HHN             Yes                  0           0:00
    ##    travel_time_num travel_time planning_time_num planning_time
    ## 1                0        0:00                 0          0:00
    ## 2                0        0:00                 0          0:00
    ## 3                0        0:00                 0          0:00
    ## 4                0        0:00                 0          0:00
    ## 5                0        0:00                 0          0:00
    ## 6                0        0:00                 0          0:00
    ## 7                0        0:00                 0          0:00
    ## 8                0        0:00                 0          0:00
    ## 9                0        0:00                 0          0:00
    ## 10               0        0:00                 0          0:00
    ## 11               0        0:00                 0          0:00
    ## 12               0        0:00                 0          0:00
    ## 13               0        0:00                 0          0:00
    ## 14               0        0:00                 0          0:00
    ## 15               0        0:00                 0          0:00
    ## 16               0        0:00                 0          0:00
    ## 17               0        0:00                 0          0:00
    ## 18               0        0:00                 0          0:00
    ## 19               0        0:00                 0          0:00
    ## 20               0        0:00                 0          0:00
    ##    total_duration_num total_duration       reason_for_no_show is_billable zip
    ## 1                   0           0:00                                FALSE   0
    ## 2                   2           0:02                                FALSE 681
    ## 3                  61           1:01                                FALSE 681
    ## 4                   0           0:00 Client No Show - No Call       FALSE 681
    ## 5                  60           1:00                                FALSE 681
    ## 6                  90           1:30                                FALSE 681
    ## 7                   4           0:04                                FALSE 681
    ## 8                   2           0:02                                FALSE 681
    ## 9                  62           1:02                                FALSE 681
    ## 10                125           2:05                                FALSE 681
    ## 11                  0           0:00                                FALSE 681
    ## 12                 61           1:01                                FALSE 681
    ## 13                  0           0:00            Client Failed       FALSE 681
    ## 14                  3           0:03                                FALSE 681
    ## 15                 60           1:00                                FALSE 681
    ## 16                 61           1:01                                FALSE 681
    ## 17                  2           0:02                                FALSE 681
    ## 18                 60           1:00                                FALSE 681
    ## 19                  2           0:02                                FALSE 681
    ## 20                  0           0:00            Client Failed       FALSE 681
    ##    state age recordID simple_race             ethnic_identity gender_identity
    ## 1     IA  12      298           8 Not Spanish/Hispanic/Latino    Not Obtained
    ## 2     NE  26      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 3     NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 4     NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 5     NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 6     NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 7     NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 8     NE  26      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 9     NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 10    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 11    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 12    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 13    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 14    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 15    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 16    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 17    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 18    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 19    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ## 20    NE  25      338          16 Not Spanish/Hispanic/Latino            <NA>
    ##    sexual_orientation
    ## 1        Not Obtained
    ## 2                <NA>
    ## 3                <NA>
    ## 4                <NA>
    ## 5                <NA>
    ## 6                <NA>
    ## 7                <NA>
    ## 8                <NA>
    ## 9                <NA>
    ## 10               <NA>
    ## 11               <NA>
    ## 12               <NA>
    ## 13               <NA>
    ## 14               <NA>
    ## 15               <NA>
    ## 16               <NA>
    ## 17               <NA>
    ## 18               <NA>
    ## 19               <NA>
    ## 20               <NA>

<br>

### 1 Two Scatter plots of two different variables, properly labelled

##### a) Scatter plot of RecordID vs Application Status

    ggplot(serdat, aes(x =recordID , y =submitted,color = submitted)) + geom_point(size=0.1)+
    labs(x="RecordID", y="Application Status", title = "Scatter plot based on RecordID and Application Status")

![](DataExploration_files/figure-markdown_strict/unnamed-chunk-2-1.png)

###### Observations :

-   From the above Scatter plot we can see the status of submitted and
    Approved applications for different record ids.
-   Apart from those two, we also have another coloumn for ‘Blank’
    status. This is where data cleaning is required. We can clean the
    data based on the columns duration and actual\_date.

##### b) Scatter plot of Age vs Program

    s2 <- ggplot(serdat, aes(x =age , y =program_name,color = program_name)) + geom_point(size=1)+
      labs(x="Age", y="Program Name", title = "Scatter plot based on Age and program description")
    s2

![](DataExploration_files/figure-markdown_strict/unnamed-chunk-3-1.png)
###### Observations :

-   The above scatter plot is between Age and Program Name.
-   From the above data we can see that the program Mental health is
    having people of all ages enrolled in it.
-   For the substance use we can see that the most people of age above
    21 are enrolling in it, the interesting point here is there are
    people of age below 21 involving in substance use which is illegal
    in USA.
-   For gambling, people of age around 30 and 50 are enrolling.

<br>

### 2 One faceted plot of two variables, properly labelled

##### Plot of Age and Mental Health, faceted by State

    ggplot(serdat, aes(x =age , y =program_name , color= program_name))+ geom_point(size = 1) +
    facet_wrap(~state)+labs(x="Age", y="Program Name", title = "Bar plot based on Age and program description")

![](DataExploration_files/figure-markdown_strict/unnamed-chunk-4-1.png)

###### Observations :

-   The above plot is between Age and Program Name which is same as 1b
    but faceted by State.
-   From this plot we can observe that the people from states SC, CO and
    NC are involving only in Mental health programs.
-   The patients in NE of age below 21 are more than in IA.
-   Among all the three programs, gambling service is being used less in
    all the states.

<br>

### 3 One bar chart, properly labeled

##### Bar chart of Count of patients w.r.t States

    serdat$state <- factor(serdat$state, levels=c("IA", "NE", "SC", "CO", "NC"))
    ggplot(serdat, aes(x=state))+ geom_bar(Width = 1)+
    labs(x="State", y="Count of Patients", title = 'Bar chart of Count of patients w.r.t States')

    ## Warning: Ignoring unknown parameters: Width

![](DataExploration_files/figure-markdown_strict/unnamed-chunk-5-1.png)

###### Observations :

-   The above graph is between state and count of patients. In this, we
    can see the number of people enrolling state wise.
-   In this graph, we can see the states having patients of high count
    on the left and of low count on the right.
-   The order of enrollments based on state is as follows : IA, NE, SC
    Co, NC (high to low).
