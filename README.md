# TDS Data Annotator

## Objective
Create data_annotater that allows user to clean data by manually annotating it.

## Requirements
- Must use standard Django Templates
- HTML/CSS, Function over aesthetics
- Raw Fields: merchant, sku, country
- Annotation Fields: retailer, segment
- DB must enforece UNIQUE combinations of merchant, sku, and country

## Tech Stack
- Django
- SQLite
- HTML/CSS

## Assumptions
- Kept the spelling for ‘Annotater’ consistent across the app to align with reqs.
- Confirm ISO Alpha-3 for country instead of 2. 3 is data consistent.
- Need to define what’s classified as Third Party and First Party
    - In this project, because there was no indicator or descriptors, the segments for each row should be categorized by the following:
        - If merchant field contains strictly the name of the business (”Target” or “Staples”) = First Party
        - If merchant field contains ANY additional characters and/or numbers(”Target 2351”) = Third Party

## Guide
1. Navigate to `/upload` and upload a retail CSV file
2. View all records on the `/dashboard`
3. Click a record to edit/annotate, assign a retailer and segment based on previous mentioned criteria
4. Go back to dashboard and toggle views to see all or filtered records.


## Trade-Offs
- Went with ModelForm for the automatic field generation. Form would be completely manual and BaseFormSet is for handling multiple forms at once.
- Chose Function views because its more direct in that you write everything that will happen. Class-based would be utilizing pre-built classes that contains abstraction instead of control.

## Enhancements:
- Refactor spelling of Annotator
- Create Async task to parse CSV
    - In the event of an extra large file this allows user freedom instead of waiting.
- Define common merchant string combinations and automate annotation. Have user validate if data was properly cleaned.
    - Includes converting all strings to lowercase for case insensitivity for automation.
    - Automating the annotating of all merchants that follow this naming format "MERCHANT ####", Merchant followed by 4 digits. This was used in the showcase as correctly marked as third party, so can be easy win.
- Validate Headers of CSV.
    - Return an error message stating improper headers to avoid crashing.
- Styling
    - Major GUI overhaul using React frontend for more dynamic UI
- If dealing with Large Datasets, utilize a dict and add SKUs that already exists. Separate dicts for each available country. Key: SKU Value: Merchant name.
    - If dict contains SKU during lookup, skip database insert. else, insert to db and add to dict. This will improve processing times. Avoids hitting database for each SKU.
