# Cockatrice Deck Generator

This is a flask web application that allows users to generate a Magic: The Gathering deck from a CSV file of cards.
The user can select a product code and product name to filter the list of available cards.
The application also allows the user to download their deck in a .cod file format for use with the Cockatrice deck-building software.
Currently limited to the preconstructed Commander decklists; more functinality will be added in the future.

## Functionality

The application has the following functionality:

- Display a list of unique product codes and product names from a CSV file of cards
- Filter the list of cards by product code and product name
- Display the current deck and its total card count
- Download the current deck in a .cod file format