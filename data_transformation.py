import apache_beam as beam
import pandas as pd
from pycountry_convert import country_alpha2_to_country_name


class MissingValueFilter(beam.DoFn):
    def process(self, element):
        """
        Filter out rows with missing values.

        Args:
            element (dict): A dictionary representing a row of data.

        Returns:
            list: A list containing the filtered row or an empty list if values are missing.
        """
        if all(value is not None and value != '' for value in element.values()):
            return [element]  # All values are not missing, keep the row
        else:
            return []  # Row has missing values, filter it out


class TextColumnCleaner(beam.DoFn):
    def process(self, element):
        """
        Clean text columns by stripping whitespace.

        Args:
            element (dict): A dictionary representing a row of data.

        Returns:
            list: A list containing the cleaned row.
        """
        for key, value in element.items():
            if isinstance(value, str):  # Check if the value is a string
                element[key] = value.strip()  # Apply .strip() to clean the string

        return [element]


class TransformData(beam.DoFn):
    partner_id_mapping = {}
    next_partner_id = 1

    def process(self, element):
        """
        Transform and normalize data.

        Args:
            element (dict): A dictionary representing a row of data.

        Returns:
            list: A list containing the transformed data.
        """
        # Format the 'date' column as a string in the desired format
        element['date'] = pd.to_datetime(element['date'], format='%Y-%m-%d')
        element['date_key'] = int(element['date'].strftime('%Y%m%d'))

        # Normalize 'country' column using country_converter
        try:
            country_name = country_alpha2_to_country_name(element['country'])
            if country_name:
                element['country_normalized'] = country_name
            else:
                element['country_normalized'] = 'Other'
        except Exception as e:
            element['country_normalized'] = 'Other'

        # Combine partner name and country to create a unique key
        partner_key = f"{element['partner']}_{element['country_normalized']}"

        # Assign a unique partner_id based on the partner name and country
        if partner_key not in self.partner_id_mapping:
            self.partner_id_mapping[partner_key] = self.next_partner_id
            self.next_partner_id += 1

        element['partner_id'] = self.partner_id_mapping[partner_key]

        transformed_data = {
            'date_key': element['date_key'],
            'partner_id': element['partner_id'],
            'partner': element['partner'],
            'partner_type': element['partner_type'],
            'country': element['country_normalized'],
            'unique_clicks': int(element['unique_clicks']),
            'new_registrations': int(element['new_registrations']),
            'first_time_depositing': int(element['first_time_depositing']),
            'cpa_triggered': int(element['cpa_triggered']),
            'cpa_earnings_eur': float(element['cpa_earnings_eur']),
            'rev_share_earnings_eur': float(element['rev_share_earnings_eur']),
            'amount_deposited_eur': float(element['amount_deposited_eur']),
            'net_revenue_eur': float(element['net_revenue_eur']),
        }
        return [transformed_data]
