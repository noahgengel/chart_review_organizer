# Chart Review Organizer

Last updated: 2021/06/14

Chart review organizer is used for the following purposes:
- Remove redundant / unnecessary: co-morbidities, indications for TNE,
complications, esophageal procedures, laryngeal procedures, abnormal
esophageal endoscopic findings, abnormal esophageal biopsy findings

- Create objects for the different rows to enable easier data analytics

NOTE: This application is specifically for the TNE project but can be repurposed
for future chart reviews.

Test cases passed:
- Successfully mapping co-morbidities
    - This includes mapping to a "deletion"
    - This includes two previously distinct co-morbidities to a single co-morbidity
- Successfully mapping the indication for a TNE
    - This includes mapping to a "deletion"
- Successfully mapping abnormal biopsy results
