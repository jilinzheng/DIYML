# Jilin Zheng // U49258796

## 240212 Notes for Modules

- Allow passing EITHER ID OR the dataset name to target_dataset, target_data, etc. (anything that might need an ID)
- Not familiar enough with ML training to do much in training module...need to inquire where I can learn more...

## Preliminary API Definition

(CRUD: C-Create, R-Read, U-Update, D-Delete)

Data Upload Module:

- (C) CreateDataset
- (U) UploadDataset
- (D) DeleteDataset
- (C) CreateLabel
- (U) AddLabel
- (U) RemoveLabel (remove label from specific data)
- (D) DeleteLabel (delete a label listing entirely)

Training Module:

- (C) CreateTrainingPoint
- (U) AddTrainingPoint
- (U) RemoveTrainingPoint
- (D) DeleteTrainingPoint
- (U) SetTrainingConfig
- (R) GetTrainingResults
