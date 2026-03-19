"""Complete country data for all 195 UN member states plus major territories"""

COUNTRIES = [
    # ==================== NORTH AMERICA ====================
    {
        'code': 'USA',
        'name': 'United States',
        'capital': 'Washington, D.C.',
        'region': 'Americas',
        'subregion': 'North America',
        'population': 333000000,
        'area': 9833517,
        'gdp': 25462,
        'languages': ['English'],
        'currencies': [{'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}],
        'timezones': ['UTC-5 to UTC-10'],
        'exports': [
            {'product': 'Machinery', 'value': 150.2, 'percentage': 18.5},
            {'product': 'Electronics', 'value': 135.8, 'percentage': 16.7},
            {'product': 'Aircraft', 'value': 120.5, 'percentage': 14.8},
            {'product': 'Vehicles', 'value': 110.3, 'percentage': 13.6},
            {'product': 'Medical Instruments', 'value': 85.2, 'percentage': 10.5},
            {'product': 'Chemicals', 'value': 70.1, 'percentage': 8.6},
            {'product': 'Plastics', 'value': 45.6, 'percentage': 5.6},
            {'product': 'Other', 'value': 95.3, 'percentage': 11.7}
        ]
    },
    {
        'code': 'CAN',
        'name': 'Canada',
        'capital': 'Ottawa',
        'region': 'Americas',
        'subregion': 'North America',
        'population': 38250000,
        'area': 9984670,
        'gdp': 2139,
        'languages': ['English', 'French'],
        'currencies': [{'name': 'Canadian Dollar', 'symbol': '$', 'code': 'CAD'}],
        'timezones': ['UTC-3:30 to UTC-8'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 120.5, 'percentage': 20.0},
            {'product': 'Vehicles', 'value': 85.3, 'percentage': 14.0},
            {'product': 'Machinery', 'value': 70.2, 'percentage': 11.5},
            {'product': 'Natural Gas', 'value': 60.8, 'percentage': 10.0},
            {'product': 'Gold', 'value': 50.1, 'percentage': 8.5},
            {'product': 'Wood', 'value': 45.6, 'percentage': 7.5},
            {'product': 'Other', 'value': 170.5, 'percentage': 28.5}
        ]
    },
    {
        'code': 'MEX',
        'name': 'Mexico',
        'capital': 'Mexico City',
        'region': 'Americas',
        'subregion': 'North America',
        'population': 128900000,
        'area': 1964375,
        'gdp': 1414,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Mexican Peso', 'symbol': '$', 'code': 'MXN'}],
        'timezones': ['UTC-5 to UTC-8'],
        'exports': [
            {'product': 'Vehicles', 'value': 90.5, 'percentage': 18.0},
            {'product': 'Electronics', 'value': 85.3, 'percentage': 17.0},
            {'product': 'Machinery', 'value': 75.2, 'percentage': 15.0},
            {'product': 'Oil', 'value': 60.8, 'percentage': 12.0},
            {'product': 'Other', 'value': 190.2, 'percentage': 38.0}
        ]
    },

    # ==================== CENTRAL AMERICA ====================
    {
        'code': 'BLZ',
        'name': 'Belize',
        'capital': 'Belmopan',
        'region': 'Americas',
        'subregion': 'Central America',
        'population': 410000,
        'area': 22966,
        'gdp': 2.5,
        'languages': ['English'],
        'currencies': [{'name': 'Belize Dollar', 'symbol': '$', 'code': 'BZD'}],
        'timezones': ['UTC-6'],
        'exports': [
            {'product': 'Sugar', 'value': 0.8, 'percentage': 30.0},
            {'product': 'Bananas', 'value': 0.5, 'percentage': 20.0},
            {'product': 'Other', 'value': 1.2, 'percentage': 50.0}
        ]
    },
    {
        'code': 'CRI',
        'name': 'Costa Rica',
        'capital': 'San José',
        'region': 'Americas',
        'subregion': 'Central America',
        'population': 5200000,
        'area': 51100,
        'gdp': 69,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Costa Rican Colón', 'symbol': '₡', 'code': 'CRC'}],
        'timezones': ['UTC-6'],
        'exports': [
            {'product': 'Electronics', 'value': 15.2, 'percentage': 35.0},
            {'product': 'Agricultural', 'value': 12.5, 'percentage': 28.0},
            {'product': 'Medical Devices', 'value': 8.3, 'percentage': 19.0},
            {'product': 'Other', 'value': 8.0, 'percentage': 18.0}
        ]
    },
    {
        'code': 'SLV',
        'name': 'El Salvador',
        'capital': 'San Salvador',
        'region': 'Americas',
        'subregion': 'Central America',
        'population': 6500000,
        'area': 21041,
        'gdp': 32,
        'languages': ['Spanish'],
        'currencies': [{'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}],
        'timezones': ['UTC-6'],
        'exports': [
            {'product': 'Textiles', 'value': 8.5, 'percentage': 40.0},
            {'product': 'Agricultural', 'value': 5.2, 'percentage': 25.0},
            {'product': 'Other', 'value': 7.3, 'percentage': 35.0}
        ]
    },
    {
        'code': 'GTM',
        'name': 'Guatemala',
        'capital': 'Guatemala City',
        'region': 'Americas',
        'subregion': 'Central America',
        'population': 17900000,
        'area': 108889,
        'gdp': 95,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Guatemalan Quetzal', 'symbol': 'Q', 'code': 'GTQ'}],
        'timezones': ['UTC-6'],
        'exports': [
            {'product': 'Agricultural', 'value': 15.2, 'percentage': 35.0},
            {'product': 'Textiles', 'value': 8.5, 'percentage': 20.0},
            {'product': 'Other', 'value': 19.3, 'percentage': 45.0}
        ]
    },
    {
        'code': 'HND',
        'name': 'Honduras',
        'capital': 'Tegucigalpa',
        'region': 'Americas',
        'subregion': 'Central America',
        'population': 10000000,
        'area': 112492,
        'gdp': 32,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Honduran Lempira', 'symbol': 'L', 'code': 'HNL'}],
        'timezones': ['UTC-6'],
        'exports': [
            {'product': 'Textiles', 'value': 8.2, 'percentage': 35.0},
            {'product': 'Coffee', 'value': 5.5, 'percentage': 23.0},
            {'product': 'Other', 'value': 10.3, 'percentage': 42.0}
        ]
    },
    {
        'code': 'NIC',
        'name': 'Nicaragua',
        'capital': 'Managua',
        'region': 'Americas',
        'subregion': 'Central America',
        'population': 6700000,
        'area': 130373,
        'gdp': 16,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Nicaraguan Córdoba', 'symbol': 'C$', 'code': 'NIO'}],
        'timezones': ['UTC-6'],
        'exports': [
            {'product': 'Agricultural', 'value': 4.2, 'percentage': 40.0},
            {'product': 'Textiles', 'value': 3.1, 'percentage': 30.0},
            {'product': 'Other', 'value': 3.7, 'percentage': 30.0}
        ]
    },
    {
        'code': 'PAN',
        'name': 'Panama',
        'capital': 'Panama City',
        'region': 'Americas',
        'subregion': 'Central America',
        'population': 4400000,
        'area': 75147,
        'gdp': 76,
        'languages': ['Spanish'],
        'currencies': [
            {'name': 'Panamanian Balboa', 'symbol': 'B/.', 'code': 'PAB'},
            {'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}
        ],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Services', 'value': 25.2, 'percentage': 45.0},
            {'product': 'Agricultural', 'value': 12.5, 'percentage': 22.0},
            {'product': 'Other', 'value': 18.3, 'percentage': 33.0}
        ]
    },

    # ==================== CARIBBEAN ====================
    {
        'code': 'ATG',
        'name': 'Antigua and Barbuda',
        'capital': "St. John's",
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 98000,
        'area': 443,
        'gdp': 1.8,
        'languages': ['English'],
        'currencies': [{'name': 'East Caribbean Dollar', 'symbol': '$', 'code': 'XCD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Tourism', 'value': 0.8, 'percentage': 60.0},
            {'product': 'Other', 'value': 0.5, 'percentage': 40.0}
        ]
    },
    {
        'code': 'BHS',
        'name': 'Bahamas',
        'capital': 'Nassau',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 400000,
        'area': 13878,
        'gdp': 14,
        'languages': ['English'],
        'currencies': [{'name': 'Bahamian Dollar', 'symbol': '$', 'code': 'BSD'}],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Tourism', 'value': 8.2, 'percentage': 70.0},
            {'product': 'Other', 'value': 3.8, 'percentage': 30.0}
        ]
    },
    {
        'code': 'BRB',
        'name': 'Barbados',
        'capital': 'Bridgetown',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 290000,
        'area': 430,
        'gdp': 5.4,
        'languages': ['English'],
        'currencies': [{'name': 'Barbadian Dollar', 'symbol': '$', 'code': 'BBD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Tourism', 'value': 2.2, 'percentage': 60.0},
            {'product': 'Rum', 'value': 0.8, 'percentage': 22.0},
            {'product': 'Other', 'value': 0.7, 'percentage': 18.0}
        ]
    },
    {
        'code': 'CUB',
        'name': 'Cuba',
        'capital': 'Havana',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 11300000,
        'area': 109884,
        'gdp': 107,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Cuban Peso', 'symbol': '$', 'code': 'CUP'}],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Medical Services', 'value': 25.2, 'percentage': 40.0},
            {'product': 'Nickel', 'value': 15.5, 'percentage': 25.0},
            {'product': 'Other', 'value': 22.3, 'percentage': 35.0}
        ]
    },
    {
        'code': 'DMA',
        'name': 'Dominica',
        'capital': 'Roseau',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 72000,
        'area': 751,
        'gdp': 0.6,
        'languages': ['English'],
        'currencies': [{'name': 'East Caribbean Dollar', 'symbol': '$', 'code': 'XCD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Agricultural', 'value': 0.3, 'percentage': 50.0},
            {'product': 'Other', 'value': 0.3, 'percentage': 50.0}
        ]
    },
    {
        'code': 'DOM',
        'name': 'Dominican Republic',
        'capital': 'Santo Domingo',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 10900000,
        'area': 48671,
        'gdp': 113,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Dominican Peso', 'symbol': '$', 'code': 'DOP'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Gold', 'value': 15.2, 'percentage': 25.0},
            {'product': 'Medical Devices', 'value': 12.5, 'percentage': 20.0},
            {'product': 'Agricultural', 'value': 10.3, 'percentage': 17.0},
            {'product': 'Other', 'value': 23.0, 'percentage': 38.0}
        ]
    },
    {
        'code': 'GRD',
        'name': 'Grenada',
        'capital': "St. George's",
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 113000,
        'area': 344,
        'gdp': 1.2,
        'languages': ['English'],
        'currencies': [{'name': 'East Caribbean Dollar', 'symbol': '$', 'code': 'XCD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Nutmeg', 'value': 0.4, 'percentage': 40.0},
            {'product': 'Other', 'value': 0.6, 'percentage': 60.0}
        ]
    },
    {
        'code': 'HTI',
        'name': 'Haiti',
        'capital': 'Port-au-Prince',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 11500000,
        'area': 27750,
        'gdp': 20,
        'languages': ['French', 'Haitian Creole'],
        'currencies': [{'name': 'Haitian Gourde', 'symbol': 'G', 'code': 'HTG'}],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Textiles', 'value': 5.2, 'percentage': 45.0},
            {'product': 'Agricultural', 'value': 3.5, 'percentage': 30.0},
            {'product': 'Other', 'value': 3.3, 'percentage': 25.0}
        ]
    },
    {
        'code': 'JAM',
        'name': 'Jamaica',
        'capital': 'Kingston',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 3000000,
        'area': 10991,
        'gdp': 15,
        'languages': ['English'],
        'currencies': [{'name': 'Jamaican Dollar', 'symbol': '$', 'code': 'JMD'}],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Alumina', 'value': 4.2, 'percentage': 35.0},
            {'product': 'Tourism', 'value': 3.5, 'percentage': 29.0},
            {'product': 'Other', 'value': 4.3, 'percentage': 36.0}
        ]
    },
    {
        'code': 'KNA',
        'name': 'Saint Kitts and Nevis',
        'capital': 'Basseterre',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 54000,
        'area': 261,
        'gdp': 1.1,
        'languages': ['English'],
        'currencies': [{'name': 'East Caribbean Dollar', 'symbol': '$', 'code': 'XCD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Tourism', 'value': 0.5, 'percentage': 55.0},
            {'product': 'Other', 'value': 0.4, 'percentage': 45.0}
        ]
    },
    {
        'code': 'LCA',
        'name': 'Saint Lucia',
        'capital': 'Castries',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 184000,
        'area': 616,
        'gdp': 2.1,
        'languages': ['English'],
        'currencies': [{'name': 'East Caribbean Dollar', 'symbol': '$', 'code': 'XCD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Tourism', 'value': 1.0, 'percentage': 60.0},
            {'product': 'Bananas', 'value': 0.4, 'percentage': 24.0},
            {'product': 'Other', 'value': 0.3, 'percentage': 16.0}
        ]
    },
    {
        'code': 'VCT',
        'name': 'Saint Vincent and the Grenadines',
        'capital': 'Kingstown',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 111000,
        'area': 389,
        'gdp': 0.9,
        'languages': ['English'],
        'currencies': [{'name': 'East Caribbean Dollar', 'symbol': '$', 'code': 'XCD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Agricultural', 'value': 0.4, 'percentage': 50.0},
            {'product': 'Other', 'value': 0.4, 'percentage': 50.0}
        ]
    },
    {
        'code': 'TTO',
        'name': 'Trinidad and Tobago',
        'capital': 'Port of Spain',
        'region': 'Americas',
        'subregion': 'Caribbean',
        'population': 1400000,
        'area': 5130,
        'gdp': 27,
        'languages': ['English'],
        'currencies': [{'name': 'Trinidad and Tobago Dollar', 'symbol': '$', 'code': 'TTD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Oil & Gas', 'value': 12.2, 'percentage': 55.0},
            {'product': 'Chemicals', 'value': 5.5, 'percentage': 25.0},
            {'product': 'Other', 'value': 4.3, 'percentage': 20.0}
        ]
    },

    # ==================== SOUTH AMERICA ====================
    {
        'code': 'ARG',
        'name': 'Argentina',
        'capital': 'Buenos Aires',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 45200000,
        'area': 2780400,
        'gdp': 641,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Argentine Peso', 'symbol': '$', 'code': 'ARS'}],
        'timezones': ['UTC-3'],
        'exports': [
            {'product': 'Soybeans', 'value': 45.2, 'percentage': 18.0},
            {'product': 'Corn', 'value': 35.5, 'percentage': 14.0},
            {'product': 'Wheat', 'value': 25.8, 'percentage': 10.0},
            {'product': 'Vehicles', 'value': 20.3, 'percentage': 8.0},
            {'product': 'Other', 'value': 128.2, 'percentage': 50.0}
        ]
    },
    {
        'code': 'BOL',
        'name': 'Bolivia',
        'capital': 'Sucre',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 11700000,
        'area': 1098581,
        'gdp': 43,
        'languages': ['Spanish', 'Quechua', 'Aymara'],
        'currencies': [{'name': 'Bolivian Boliviano', 'symbol': 'Bs.', 'code': 'BOB'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Natural Gas', 'value': 12.2, 'percentage': 35.0},
            {'product': 'Silver', 'value': 8.5, 'percentage': 24.0},
            {'product': 'Zinc', 'value': 5.3, 'percentage': 15.0},
            {'product': 'Other', 'value': 9.0, 'percentage': 26.0}
        ]
    },
    {
        'code': 'BRA',
        'name': 'Brazil',
        'capital': 'Brasília',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 213000000,
        'area': 8515767,
        'gdp': 1920,
        'languages': ['Portuguese'],
        'currencies': [{'name': 'Brazilian Real', 'symbol': 'R$', 'code': 'BRL'}],
        'timezones': ['UTC-2 to UTC-5'],
        'exports': [
            {'product': 'Soybeans', 'value': 85.4, 'percentage': 15.0},
            {'product': 'Iron Ore', 'value': 75.2, 'percentage': 13.0},
            {'product': 'Crude Petroleum', 'value': 65.8, 'percentage': 11.5},
            {'product': 'Sugar', 'value': 50.3, 'percentage': 9.0},
            {'product': 'Poultry', 'value': 45.1, 'percentage': 8.0},
            {'product': 'Other', 'value': 251.2, 'percentage': 43.5}
        ]
    },
    {
        'code': 'CHL',
        'name': 'Chile',
        'capital': 'Santiago',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 19100000,
        'area': 756102,
        'gdp': 317,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Chilean Peso', 'symbol': '$', 'code': 'CLP'}],
        'timezones': ['UTC-3 to UTC-5'],
        'exports': [
            {'product': 'Copper', 'value': 85.2, 'percentage': 45.0},
            {'product': 'Fruit', 'value': 25.5, 'percentage': 13.0},
            {'product': 'Salmon', 'value': 20.8, 'percentage': 11.0},
            {'product': 'Other', 'value': 60.5, 'percentage': 31.0}
        ]
    },
    {
        'code': 'COL',
        'name': 'Colombia',
        'capital': 'Bogotá',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 50800000,
        'area': 1141748,
        'gdp': 351,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Colombian Peso', 'symbol': '$', 'code': 'COP'}],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Crude Oil', 'value': 65.2, 'percentage': 30.0},
            {'product': 'Coal', 'value': 35.5, 'percentage': 16.0},
            {'product': 'Coffee', 'value': 25.8, 'percentage': 12.0},
            {'product': 'Gold', 'value': 20.3, 'percentage': 9.0},
            {'product': 'Other', 'value': 72.2, 'percentage': 33.0}
        ]
    },
    {
        'code': 'ECU',
        'name': 'Ecuador',
        'capital': 'Quito',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 17600000,
        'area': 283561,
        'gdp': 115,
        'languages': ['Spanish'],
        'currencies': [{'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Crude Oil', 'value': 35.2, 'percentage': 35.0},
            {'product': 'Bananas', 'value': 20.5, 'percentage': 20.0},
            {'product': 'Shrimp', 'value': 18.8, 'percentage': 18.0},
            {'product': 'Other', 'value': 28.5, 'percentage': 27.0}
        ]
    },
    {
        'code': 'GUY',
        'name': 'Guyana',
        'capital': 'Georgetown',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 790000,
        'area': 214969,
        'gdp': 15,
        'languages': ['English'],
        'currencies': [{'name': 'Guyanese Dollar', 'symbol': '$', 'code': 'GYD'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Gold', 'value': 3.2, 'percentage': 35.0},
            {'product': 'Oil', 'value': 2.8, 'percentage': 30.0},
            {'product': 'Other', 'value': 3.0, 'percentage': 35.0}
        ]
    },
    {
        'code': 'PRY',
        'name': 'Paraguay',
        'capital': 'Asunción',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 7300000,
        'area': 406752,
        'gdp': 42,
        'languages': ['Spanish', 'Guaraní'],
        'currencies': [{'name': 'Paraguayan Guaraní', 'symbol': '₲', 'code': 'PYG'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Soybeans', 'value': 12.2, 'percentage': 35.0},
            {'product': 'Beef', 'value': 8.5, 'percentage': 24.0},
            {'product': 'Corn', 'value': 5.3, 'percentage': 15.0},
            {'product': 'Other', 'value': 9.0, 'percentage': 26.0}
        ]
    },
    {
        'code': 'PER',
        'name': 'Peru',
        'capital': 'Lima',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 33000000,
        'area': 1285216,
        'gdp': 264,
        'languages': ['Spanish', 'Quechua', 'Aymara'],
        'currencies': [{'name': 'Peruvian Sol', 'symbol': 'S/', 'code': 'PEN'}],
        'timezones': ['UTC-5'],
        'exports': [
            {'product': 'Copper', 'value': 45.2, 'percentage': 25.0},
            {'product': 'Gold', 'value': 35.5, 'percentage': 20.0},
            {'product': 'Zinc', 'value': 20.8, 'percentage': 12.0},
            {'product': 'Other', 'value': 78.5, 'percentage': 43.0}
        ]
    },
    {
        'code': 'SUR',
        'name': 'Suriname',
        'capital': 'Paramaribo',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 590000,
        'area': 163820,
        'gdp': 3.5,
        'languages': ['Dutch'],
        'currencies': [{'name': 'Surinamese Dollar', 'symbol': '$', 'code': 'SRD'}],
        'timezones': ['UTC-3'],
        'exports': [
            {'product': 'Gold', 'value': 1.2, 'percentage': 40.0},
            {'product': 'Oil', 'value': 0.8, 'percentage': 27.0},
            {'product': 'Other', 'value': 1.0, 'percentage': 33.0}
        ]
    },
    {
        'code': 'URY',
        'name': 'Uruguay',
        'capital': 'Montevideo',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 3500000,
        'area': 176215,
        'gdp': 77,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Uruguayan Peso', 'symbol': '$', 'code': 'UYU'}],
        'timezones': ['UTC-3'],
        'exports': [
            {'product': 'Beef', 'value': 15.2, 'percentage': 28.0},
            {'product': 'Soybeans', 'value': 12.5, 'percentage': 23.0},
            {'product': 'Wood', 'value': 10.8, 'percentage': 20.0},
            {'product': 'Other', 'value': 15.5, 'percentage': 29.0}
        ]
    },
    {
        'code': 'VEN',
        'name': 'Venezuela',
        'capital': 'Caracas',
        'region': 'Americas',
        'subregion': 'South America',
        'population': 28400000,
        'area': 916445,
        'gdp': 96,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Venezuelan Bolívar', 'symbol': 'Bs.', 'code': 'VES'}],
        'timezones': ['UTC-4'],
        'exports': [
            {'product': 'Crude Oil', 'value': 45.2, 'percentage': 75.0},
            {'product': 'Other', 'value': 15.8, 'percentage': 25.0}
        ]
    },

    # ==================== EUROPE ====================
    {
        'code': 'ALB',
        'name': 'Albania',
        'capital': 'Tirana',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 2800000,
        'area': 28748,
        'gdp': 18,
        'languages': ['Albanian'],
        'currencies': [{'name': 'Albanian Lek', 'symbol': 'L', 'code': 'ALL'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Textiles', 'value': 3.2, 'percentage': 30.0},
            {'product': 'Minerals', 'value': 2.5, 'percentage': 23.0},
            {'product': 'Other', 'value': 5.3, 'percentage': 47.0}
        ]
    },
    {
        'code': 'AND',
        'name': 'Andorra',
        'capital': 'Andorra la Vella',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 78000,
        'area': 468,
        'gdp': 3.4,
        'languages': ['Catalan'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Tourism', 'value': 1.5, 'percentage': 60.0},
            {'product': 'Other', 'value': 1.0, 'percentage': 40.0}
        ]
    },
    {
        'code': 'AUT',
        'name': 'Austria',
        'capital': 'Vienna',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 9000000,
        'area': 83871,
        'gdp': 520,
        'languages': ['German'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 45.3, 'percentage': 25.0},
            {'product': 'Vehicles', 'value': 35.2, 'percentage': 19.0},
            {'product': 'Pharmaceuticals', 'value': 25.8, 'percentage': 14.0},
            {'product': 'Other', 'value': 76.7, 'percentage': 42.0}
        ]
    },
    {
        'code': 'BLR',
        'name': 'Belarus',
        'capital': 'Minsk',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 9400000,
        'area': 207600,
        'gdp': 68,
        'languages': ['Belarusian', 'Russian'],
        'currencies': [{'name': 'Belarusian Ruble', 'symbol': 'Br', 'code': 'BYN'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Machinery', 'value': 15.3, 'percentage': 28.0},
            {'product': 'Chemicals', 'value': 12.2, 'percentage': 22.0},
            {'product': 'Other', 'value': 27.5, 'percentage': 50.0}
        ]
    },
    {
        'code': 'BEL',
        'name': 'Belgium',
        'capital': 'Brussels',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 11600000,
        'area': 30528,
        'gdp': 609,
        'languages': ['Dutch', 'French', 'German'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Chemicals', 'value': 45.3, 'percentage': 22.0},
            {'product': 'Machinery', 'value': 35.2, 'percentage': 17.0},
            {'product': 'Pharmaceuticals', 'value': 30.8, 'percentage': 15.0},
            {'product': 'Other', 'value': 94.7, 'percentage': 46.0}
        ]
    },
    {
        'code': 'BIH',
        'name': 'Bosnia and Herzegovina',
        'capital': 'Sarajevo',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 3300000,
        'area': 51197,
        'gdp': 23,
        'languages': ['Bosnian', 'Croatian', 'Serbian'],
        'currencies': [{'name': 'Convertible Mark', 'symbol': 'KM', 'code': 'BAM'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 4.3, 'percentage': 25.0},
            {'product': 'Textiles', 'value': 3.5, 'percentage': 20.0},
            {'product': 'Other', 'value': 9.2, 'percentage': 55.0}
        ]
    },
    {
        'code': 'BGR',
        'name': 'Bulgaria',
        'capital': 'Sofia',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 6900000,
        'area': 110994,
        'gdp': 100,
        'languages': ['Bulgarian'],
        'currencies': [{'name': 'Bulgarian Lev', 'symbol': 'лв', 'code': 'BGN'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Machinery', 'value': 15.3, 'percentage': 24.0},
            {'product': 'Agricultural', 'value': 12.2, 'percentage': 19.0},
            {'product': 'Other', 'value': 36.5, 'percentage': 57.0}
        ]
    },
    {
        'code': 'HRV',
        'name': 'Croatia',
        'capital': 'Zagreb',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 4000000,
        'area': 56594,
        'gdp': 71,
        'languages': ['Croatian'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 10.3, 'percentage': 20.0},
            {'product': 'Pharmaceuticals', 'value': 8.2, 'percentage': 16.0},
            {'product': 'Other', 'value': 32.5, 'percentage': 64.0}
        ]
    },
    {
        'code': 'CYP',
        'name': 'Cyprus',
        'capital': 'Nicosia',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 1200000,
        'area': 9251,
        'gdp': 28,
        'languages': ['Greek', 'Turkish'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Services', 'value': 8.2, 'percentage': 45.0},
            {'product': 'Pharmaceuticals', 'value': 4.5, 'percentage': 25.0},
            {'product': 'Other', 'value': 5.3, 'percentage': 30.0}
        ]
    },
    {
        'code': 'CZE',
        'name': 'Czech Republic',
        'capital': 'Prague',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 10700000,
        'area': 78867,
        'gdp': 290,
        'languages': ['Czech'],
        'currencies': [{'name': 'Czech Koruna', 'symbol': 'Kč', 'code': 'CZK'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Vehicles', 'value': 45.3, 'percentage': 30.0},
            {'product': 'Machinery', 'value': 35.2, 'percentage': 23.0},
            {'product': 'Electronics', 'value': 25.8, 'percentage': 17.0},
            {'product': 'Other', 'value': 45.7, 'percentage': 30.0}
        ]
    },
    {
        'code': 'DNK',
        'name': 'Denmark',
        'capital': 'Copenhagen',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 5800000,
        'area': 43094,
        'gdp': 405,
        'languages': ['Danish'],
        'currencies': [{'name': 'Danish Krone', 'symbol': 'kr', 'code': 'DKK'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 35.3, 'percentage': 24.0},
            {'product': 'Pharmaceuticals', 'value': 25.2, 'percentage': 17.0},
            {'product': 'Agricultural', 'value': 20.8, 'percentage': 14.0},
            {'product': 'Other', 'value': 66.7, 'percentage': 45.0}
        ]
    },
    {
        'code': 'EST',
        'name': 'Estonia',
        'capital': 'Tallinn',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 1300000,
        'area': 45227,
        'gdp': 38,
        'languages': ['Estonian'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Electronics', 'value': 8.3, 'percentage': 28.0},
            {'product': 'Machinery', 'value': 6.5, 'percentage': 22.0},
            {'product': 'Other', 'value': 15.2, 'percentage': 50.0}
        ]
    },
    {
        'code': 'FIN',
        'name': 'Finland',
        'capital': 'Helsinki',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 5500000,
        'area': 338455,
        'gdp': 297,
        'languages': ['Finnish', 'Swedish'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Machinery', 'value': 35.3, 'percentage': 28.0},
            {'product': 'Electronics', 'value': 25.2, 'percentage': 20.0},
            {'product': 'Paper', 'value': 20.8, 'percentage': 16.0},
            {'product': 'Other', 'value': 45.7, 'percentage': 36.0}
        ]
    },
    {
        'code': 'FRA',
        'name': 'France',
        'capital': 'Paris',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 67400000,
        'area': 551695,
        'gdp': 2937,
        'languages': ['French'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Aircraft', 'value': 75.4, 'percentage': 17.0},
            {'product': 'Chemicals', 'value': 70.2, 'percentage': 15.5},
            {'product': 'Vehicles', 'value': 65.8, 'percentage': 14.5},
            {'product': 'Machinery', 'value': 60.3, 'percentage': 13.0},
            {'product': 'Pharmaceuticals', 'value': 55.1, 'percentage': 12.0},
            {'product': 'Other', 'value': 126.2, 'percentage': 28.0}
        ]
    },
    {
        'code': 'DEU',
        'name': 'Germany',
        'capital': 'Berlin',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 83200000,
        'area': 357114,
        'gdp': 4256,
        'languages': ['German'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Vehicles', 'value': 280.5, 'percentage': 21.5},
            {'product': 'Machinery', 'value': 250.3, 'percentage': 19.2},
            {'product': 'Chemicals', 'value': 200.8, 'percentage': 15.4},
            {'product': 'Electronics', 'value': 180.2, 'percentage': 13.8},
            {'product': 'Pharmaceuticals', 'value': 150.6, 'percentage': 11.5},
            {'product': 'Other', 'value': 245.6, 'percentage': 18.6}
        ]
    },
    {
        'code': 'GRC',
        'name': 'Greece',
        'capital': 'Athens',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 10400000,
        'area': 131957,
        'gdp': 222,
        'languages': ['Greek'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Oil', 'value': 25.3, 'percentage': 25.0},
            {'product': 'Agricultural', 'value': 20.2, 'percentage': 20.0},
            {'product': 'Pharmaceuticals', 'value': 15.8, 'percentage': 16.0},
            {'product': 'Other', 'value': 39.7, 'percentage': 39.0}
        ]
    },
    {
        'code': 'HUN',
        'name': 'Hungary',
        'capital': 'Budapest',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 9700000,
        'area': 93028,
        'gdp': 184,
        'languages': ['Hungarian'],
        'currencies': [{'name': 'Hungarian Forint', 'symbol': 'Ft', 'code': 'HUF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Vehicles', 'value': 35.3, 'percentage': 28.0},
            {'product': 'Electronics', 'value': 30.2, 'percentage': 24.0},
            {'product': 'Machinery', 'value': 25.8, 'percentage': 20.0},
            {'product': 'Other', 'value': 35.7, 'percentage': 28.0}
        ]
    },
    {
        'code': 'ISL',
        'name': 'Iceland',
        'capital': 'Reykjavik',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 370000,
        'area': 103000,
        'gdp': 27,
        'languages': ['Icelandic'],
        'currencies': [{'name': 'Icelandic Króna', 'symbol': 'kr', 'code': 'ISK'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Fish', 'value': 8.3, 'percentage': 45.0},
            {'product': 'Aluminum', 'value': 5.2, 'percentage': 28.0},
            {'product': 'Other', 'value': 5.5, 'percentage': 27.0}
        ]
    },
    {
        'code': 'IRL',
        'name': 'Ireland',
        'capital': 'Dublin',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 5000000,
        'area': 70273,
        'gdp': 519,
        'languages': ['Irish', 'English'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Pharmaceuticals', 'value': 85.3, 'percentage': 35.0},
            {'product': 'Electronics', 'value': 55.2, 'percentage': 23.0},
            {'product': 'Chemicals', 'value': 45.8, 'percentage': 19.0},
            {'product': 'Other', 'value': 55.7, 'percentage': 23.0}
        ]
    },
    {
        'code': 'ITA',
        'name': 'Italy',
        'capital': 'Rome',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 60300000,
        'area': 301336,
        'gdp': 2101,
        'languages': ['Italian'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 85.3, 'percentage': 18.0},
            {'product': 'Vehicles', 'value': 70.2, 'percentage': 15.0},
            {'product': 'Pharmaceuticals', 'value': 65.8, 'percentage': 14.0},
            {'product': 'Textiles', 'value': 55.4, 'percentage': 12.0},
            {'product': 'Other', 'value': 195.3, 'percentage': 41.0}
        ]
    },
    {
        'code': 'LVA',
        'name': 'Latvia',
        'capital': 'Riga',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 1900000,
        'area': 64589,
        'gdp': 41,
        'languages': ['Latvian'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Wood', 'value': 8.3, 'percentage': 30.0},
            {'product': 'Agricultural', 'value': 5.5, 'percentage': 20.0},
            {'product': 'Other', 'value': 14.2, 'percentage': 50.0}
        ]
    },
    {
        'code': 'LIE',
        'name': 'Liechtenstein',
        'capital': 'Vaduz',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 39000,
        'area': 160,
        'gdp': 6.2,
        'languages': ['German'],
        'currencies': [{'name': 'Swiss Franc', 'symbol': 'Fr', 'code': 'CHF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 2.2, 'percentage': 45.0},
            {'product': 'Other', 'value': 2.8, 'percentage': 55.0}
        ]
    },
    {
        'code': 'LTU',
        'name': 'Lithuania',
        'capital': 'Vilnius',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 2700000,
        'area': 65300,
        'gdp': 71,
        'languages': ['Lithuanian'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Agricultural', 'value': 12.3, 'percentage': 28.0},
            {'product': 'Machinery', 'value': 10.5, 'percentage': 24.0},
            {'product': 'Other', 'value': 21.2, 'percentage': 48.0}
        ]
    },
    {
        'code': 'LUX',
        'name': 'Luxembourg',
        'capital': 'Luxembourg City',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 640000,
        'area': 2586,
        'gdp': 86,
        'languages': ['Luxembourgish', 'French', 'German'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Services', 'value': 35.2, 'percentage': 55.0},
            {'product': 'Steel', 'value': 15.5, 'percentage': 24.0},
            {'product': 'Other', 'value': 13.3, 'percentage': 21.0}
        ]
    },
    {
        'code': 'MLT',
        'name': 'Malta',
        'capital': 'Valletta',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 520000,
        'area': 316,
        'gdp': 17,
        'languages': ['Maltese', 'English'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Services', 'value': 6.2, 'percentage': 45.0},
            {'product': 'Electronics', 'value': 4.5, 'percentage': 33.0},
            {'product': 'Other', 'value': 3.3, 'percentage': 22.0}
        ]
    },
    {
        'code': 'MCO',
        'name': 'Monaco',
        'capital': 'Monaco',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 39000,
        'area': 2,
        'gdp': 7.2,
        'languages': ['French'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Services', 'value': 3.2, 'percentage': 60.0},
            {'product': 'Other', 'value': 2.2, 'percentage': 40.0}
        ]
    },
    {
        'code': 'MNE',
        'name': 'Montenegro',
        'capital': 'Podgorica',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 620000,
        'area': 13812,
        'gdp': 6,
        'languages': ['Montenegrin'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Metals', 'value': 1.8, 'percentage': 35.0},
            {'product': 'Energy', 'value': 1.2, 'percentage': 24.0},
            {'product': 'Other', 'value': 2.0, 'percentage': 41.0}
        ]
    },
    {
        'code': 'NLD',
        'name': 'Netherlands',
        'capital': 'Amsterdam',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 17500000,
        'area': 41543,
        'gdp': 1013,
        'languages': ['Dutch'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 85.3, 'percentage': 18.0},
            {'product': 'Chemicals', 'value': 75.2, 'percentage': 16.0},
            {'product': 'Electronics', 'value': 65.8, 'percentage': 14.0},
            {'product': 'Agricultural', 'value': 55.4, 'percentage': 12.0},
            {'product': 'Other', 'value': 190.3, 'percentage': 40.0}
        ]
    },
    {
        'code': 'MKD',
        'name': 'North Macedonia',
        'capital': 'Skopje',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 2000000,
        'area': 25713,
        'gdp': 15,
        'languages': ['Macedonian'],
        'currencies': [{'name': 'Macedonian Denar', 'symbol': 'ден', 'code': 'MKD'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Textiles', 'value': 3.2, 'percentage': 28.0},
            {'product': 'Metals', 'value': 2.8, 'percentage': 24.0},
            {'product': 'Other', 'value': 5.0, 'percentage': 48.0}
        ]
    },
    {
        'code': 'NOR',
        'name': 'Norway',
        'capital': 'Oslo',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 5400000,
        'area': 385207,
        'gdp': 554,
        'languages': ['Norwegian'],
        'currencies': [{'name': 'Norwegian Krone', 'symbol': 'kr', 'code': 'NOK'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Oil & Gas', 'value': 85.3, 'percentage': 45.0},
            {'product': 'Fish', 'value': 35.2, 'percentage': 19.0},
            {'product': 'Machinery', 'value': 25.8, 'percentage': 14.0},
            {'product': 'Other', 'value': 40.7, 'percentage': 22.0}
        ]
    },
    {
        'code': 'POL',
        'name': 'Poland',
        'capital': 'Warsaw',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 37800000,
        'area': 312696,
        'gdp': 748,
        'languages': ['Polish'],
        'currencies': [{'name': 'Polish Złoty', 'symbol': 'zł', 'code': 'PLN'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 55.3, 'percentage': 22.0},
            {'product': 'Vehicles', 'value': 45.2, 'percentage': 18.0},
            {'product': 'Electronics', 'value': 40.8, 'percentage': 16.0},
            {'product': 'Other', 'value': 110.7, 'percentage': 44.0}
        ]
    },
    {
        'code': 'PRT',
        'name': 'Portugal',
        'capital': 'Lisbon',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 10300000,
        'area': 92090,
        'gdp': 267,
        'languages': ['Portuguese'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Vehicles', 'value': 25.3, 'percentage': 15.0},
            {'product': 'Machinery', 'value': 20.2, 'percentage': 12.0},
            {'product': 'Textiles', 'value': 18.8, 'percentage': 11.0},
            {'product': 'Other', 'value': 104.7, 'percentage': 62.0}
        ]
    },
    {
        'code': 'ROU',
        'name': 'Romania',
        'capital': 'Bucharest',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 19200000,
        'area': 238391,
        'gdp': 314,
        'languages': ['Romanian'],
        'currencies': [{'name': 'Romanian Leu', 'symbol': 'lei', 'code': 'RON'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Machinery', 'value': 35.3, 'percentage': 26.0},
            {'product': 'Vehicles', 'value': 30.2, 'percentage': 22.0},
            {'product': 'Electronics', 'value': 25.8, 'percentage': 19.0},
            {'product': 'Other', 'value': 45.7, 'percentage': 33.0}
        ]
    },
    {
        'code': 'RUS',
        'name': 'Russia',
        'capital': 'Moscow',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 145900000,
        'area': 17098242,
        'gdp': 2060,
        'languages': ['Russian'],
        'currencies': [{'name': 'Russian Ruble', 'symbol': '₽', 'code': 'RUB'}],
        'timezones': ['UTC+2 to UTC+12'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 250.8, 'percentage': 30.0},
            {'product': 'Natural Gas', 'value': 150.4, 'percentage': 18.0},
            {'product': 'Coal', 'value': 80.2, 'percentage': 9.5},
            {'product': 'Gold', 'value': 70.1, 'percentage': 8.5},
            {'product': 'Other', 'value': 285.5, 'percentage': 34.0}
        ]
    },
    {
        'code': 'SMR',
        'name': 'San Marino',
        'capital': 'San Marino',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 34000,
        'area': 61,
        'gdp': 1.6,
        'languages': ['Italian'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Services', 'value': 0.8, 'percentage': 55.0},
            {'product': 'Other', 'value': 0.6, 'percentage': 45.0}
        ]
    },
    {
        'code': 'SRB',
        'name': 'Serbia',
        'capital': 'Belgrade',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 6800000,
        'area': 77474,
        'gdp': 68,
        'languages': ['Serbian'],
        'currencies': [{'name': 'Serbian Dinar', 'symbol': 'дин', 'code': 'RSD'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Vehicles', 'value': 12.3, 'percentage': 22.0},
            {'product': 'Machinery', 'value': 10.2, 'percentage': 18.0},
            {'product': 'Other', 'value': 33.5, 'percentage': 60.0}
        ]
    },
    {
        'code': 'SVK',
        'name': 'Slovakia',
        'capital': 'Bratislava',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 5400000,
        'area': 49035,
        'gdp': 118,
        'languages': ['Slovak'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Vehicles', 'value': 25.3, 'percentage': 35.0},
            {'product': 'Electronics', 'value': 15.2, 'percentage': 21.0},
            {'product': 'Other', 'value': 31.5, 'percentage': 44.0}
        ]
    },
    {
        'code': 'SVN',
        'name': 'Slovenia',
        'capital': 'Ljubljana',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 2100000,
        'area': 20273,
        'gdp': 63,
        'languages': ['Slovene'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 12.3, 'percentage': 28.0},
            {'product': 'Pharmaceuticals', 'value': 8.5, 'percentage': 19.0},
            {'product': 'Other', 'value': 23.2, 'percentage': 53.0}
        ]
    },
    {
        'code': 'ESP',
        'name': 'Spain',
        'capital': 'Madrid',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 47400000,
        'area': 505992,
        'gdp': 1427,
        'languages': ['Spanish'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Vehicles', 'value': 65.3, 'percentage': 16.0},
            {'product': 'Machinery', 'value': 55.2, 'percentage': 14.0},
            {'product': 'Pharmaceuticals', 'value': 45.8, 'percentage': 12.0},
            {'product': 'Food Products', 'value': 40.4, 'percentage': 10.0},
            {'product': 'Other', 'value': 185.3, 'percentage': 48.0}
        ]
    },
    {
        'code': 'SWE',
        'name': 'Sweden',
        'capital': 'Stockholm',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 10400000,
        'area': 450295,
        'gdp': 621,
        'languages': ['Swedish'],
        'currencies': [{'name': 'Swedish Krona', 'symbol': 'kr', 'code': 'SEK'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Machinery', 'value': 45.3, 'percentage': 22.0},
            {'product': 'Vehicles', 'value': 35.2, 'percentage': 17.0},
            {'product': 'Pharmaceuticals', 'value': 30.8, 'percentage': 15.0},
            {'product': 'Electronics', 'value': 25.4, 'percentage': 12.0},
            {'product': 'Other', 'value': 70.3, 'percentage': 34.0}
        ]
    },
    {
        'code': 'CHE',
        'name': 'Switzerland',
        'capital': 'Bern',
        'region': 'Europe',
        'subregion': 'Western Europe',
        'population': 8700000,
        'area': 41284,
        'gdp': 841,
        'languages': ['German', 'French', 'Italian', 'Romansh'],
        'currencies': [{'name': 'Swiss Franc', 'symbol': 'Fr', 'code': 'CHF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Pharmaceuticals', 'value': 85.3, 'percentage': 30.0},
            {'product': 'Machinery', 'value': 55.2, 'percentage': 20.0},
            {'product': 'Watches', 'value': 45.8, 'percentage': 16.0},
            {'product': 'Other', 'value': 97.7, 'percentage': 34.0}
        ]
    },
    {
        'code': 'UKR',
        'name': 'Ukraine',
        'capital': 'Kyiv',
        'region': 'Europe',
        'subregion': 'Eastern Europe',
        'population': 41000000,
        'area': 603500,
        'gdp': 200,
        'languages': ['Ukrainian'],
        'currencies': [{'name': 'Ukrainian Hryvnia', 'symbol': '₴', 'code': 'UAH'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Agricultural', 'value': 45.3, 'percentage': 35.0},
            {'product': 'Iron', 'value': 30.2, 'percentage': 23.0},
            {'product': 'Machinery', 'value': 20.8, 'percentage': 16.0},
            {'product': 'Other', 'value': 33.7, 'percentage': 26.0}
        ]
    },
    {
        'code': 'GBR',
        'name': 'United Kingdom',
        'capital': 'London',
        'region': 'Europe',
        'subregion': 'Northern Europe',
        'population': 67300000,
        'area': 242900,
        'gdp': 3376,
        'languages': ['English'],
        'currencies': [{'name': 'Pound Sterling', 'symbol': '£', 'code': 'GBP'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Machinery', 'value': 85.3, 'percentage': 18.0},
            {'product': 'Chemicals', 'value': 70.2, 'percentage': 15.0},
            {'product': 'Vehicles', 'value': 65.8, 'percentage': 14.0},
            {'product': 'Aircraft', 'value': 55.4, 'percentage': 11.5},
            {'product': 'Pharmaceuticals', 'value': 50.1, 'percentage': 10.5},
            {'product': 'Other', 'value': 150.2, 'percentage': 31.0}
        ]
    },
    {
        'code': 'VAT',
        'name': 'Vatican City',
        'capital': 'Vatican City',
        'region': 'Europe',
        'subregion': 'Southern Europe',
        'population': 800,
        'area': 0.44,
        'gdp': 0.2,
        'languages': ['Italian', 'Latin'],
        'currencies': [{'name': 'Euro', 'symbol': '€', 'code': 'EUR'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Services', 'value': 0.1, 'percentage': 70.0},
            {'product': 'Other', 'value': 0.1, 'percentage': 30.0}
        ]
    },

    # ==================== ASIA ====================
    {
        'code': 'AFG',
        'name': 'Afghanistan',
        'capital': 'Kabul',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 38900000,
        'area': 652230,
        'gdp': 20,
        'languages': ['Pashto', 'Dari'],
        'currencies': [{'name': 'Afghan Afghani', 'symbol': '؋', 'code': 'AFN'}],
        'timezones': ['UTC+4:30'],
        'exports': [
            {'product': 'Fruit', 'value': 3.2, 'percentage': 35.0},
            {'product': 'Textiles', 'value': 2.5, 'percentage': 27.0},
            {'product': 'Other', 'value': 3.3, 'percentage': 38.0}
        ]
    },
    {
        'code': 'ARM',
        'name': 'Armenia',
        'capital': 'Yerevan',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 3000000,
        'area': 29743,
        'gdp': 19,
        'languages': ['Armenian'],
        'currencies': [{'name': 'Armenian Dram', 'symbol': '֏', 'code': 'AMD'}],
        'timezones': ['UTC+4'],
        'exports': [
            {'product': 'Metals', 'value': 4.2, 'percentage': 32.0},
            {'product': 'Agricultural', 'value': 3.5, 'percentage': 27.0},
            {'product': 'Other', 'value': 5.3, 'percentage': 41.0}
        ]
    },
    {
        'code': 'AZE',
        'name': 'Azerbaijan',
        'capital': 'Baku',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 10100000,
        'area': 86600,
        'gdp': 73,
        'languages': ['Azerbaijani'],
        'currencies': [{'name': 'Azerbaijani Manat', 'symbol': '₼', 'code': 'AZN'}],
        'timezones': ['UTC+4'],
        'exports': [
            {'product': 'Oil & Gas', 'value': 25.2, 'percentage': 65.0},
            {'product': 'Agricultural', 'value': 5.5, 'percentage': 14.0},
            {'product': 'Other', 'value': 8.3, 'percentage': 21.0}
        ]
    },
    {
        'code': 'BHR',
        'name': 'Bahrain',
        'capital': 'Manama',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 1700000,
        'area': 765,
        'gdp': 44,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Bahraini Dinar', 'symbol': '.د.ب', 'code': 'BHD'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Oil', 'value': 15.2, 'percentage': 55.0},
            {'product': 'Aluminum', 'value': 6.5, 'percentage': 24.0},
            {'product': 'Other', 'value': 6.3, 'percentage': 21.0}
        ]
    },
    {
        'code': 'BGD',
        'name': 'Bangladesh',
        'capital': 'Dhaka',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 165000000,
        'area': 147570,
        'gdp': 416,
        'languages': ['Bengali'],
        'currencies': [{'name': 'Bangladeshi Taka', 'symbol': '৳', 'code': 'BDT'}],
        'timezones': ['UTC+6'],
        'exports': [
            {'product': 'Textiles', 'value': 65.2, 'percentage': 75.0},
            {'product': 'Other', 'value': 21.8, 'percentage': 25.0}
        ]
    },
    {
        'code': 'BTN',
        'name': 'Bhutan',
        'capital': 'Thimphu',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 780000,
        'area': 38394,
        'gdp': 2.8,
        'languages': ['Dzongkha'],
        'currencies': [{'name': 'Bhutanese Ngultrum', 'symbol': 'Nu.', 'code': 'BTN'}],
        'timezones': ['UTC+6'],
        'exports': [
            {'product': 'Hydro', 'value': 0.8, 'percentage': 40.0},
            {'product': 'Other', 'value': 1.2, 'percentage': 60.0}
        ]
    },
    {
        'code': 'BRN',
        'name': 'Brunei',
        'capital': 'Bandar Seri Begawan',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 440000,
        'area': 5765,
        'gdp': 14,
        'languages': ['Malay'],
        'currencies': [{'name': 'Brunei Dollar', 'symbol': '$', 'code': 'BND'}],
        'timezones': ['UTC+8'],
        'exports': [
            {'product': 'Oil & Gas', 'value': 8.2, 'percentage': 85.0},
            {'product': 'Other', 'value': 1.8, 'percentage': 15.0}
        ]
    },
    {
        'code': 'KHM',
        'name': 'Cambodia',
        'capital': 'Phnom Penh',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 16700000,
        'area': 181035,
        'gdp': 28,
        'languages': ['Khmer'],
        'currencies': [{'name': 'Cambodian Riel', 'symbol': '៛', 'code': 'KHR'}],
        'timezones': ['UTC+7'],
        'exports': [
            {'product': 'Textiles', 'value': 12.2, 'percentage': 65.0},
            {'product': 'Other', 'value': 6.8, 'percentage': 35.0}
        ]
    },
    {
        'code': 'CHN',
        'name': 'China',
        'capital': 'Beijing',
        'region': 'Asia',
        'subregion': 'Eastern Asia',
        'population': 1412000000,
        'area': 9596961,
        'gdp': 17963,
        'languages': ['Mandarin'],
        'currencies': [{'name': 'Chinese Yuan', 'symbol': '¥', 'code': 'CNY'}],
        'timezones': ['UTC+8'],
        'exports': [
            {'product': 'Electronics', 'value': 350.5, 'percentage': 22.5},
            {'product': 'Machinery', 'value': 300.2, 'percentage': 19.3},
            {'product': 'Textiles', 'value': 180.7, 'percentage': 11.6},
            {'product': 'Furniture', 'value': 150.3, 'percentage': 9.7},
            {'product': 'Plastics', 'value': 120.8, 'percentage': 7.7},
            {'product': 'Toys', 'value': 100.4, 'percentage': 6.4},
            {'product': 'Vehicles', 'value': 90.2, 'percentage': 5.8},
            {'product': 'Other', 'value': 265.1, 'percentage': 17.0}
        ]
    },
    {
        'code': 'GEO',
        'name': 'Georgia',
        'capital': 'Tbilisi',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 3700000,
        'area': 69700,
        'gdp': 24,
        'languages': ['Georgian'],
        'currencies': [{'name': 'Georgian Lari', 'symbol': '₾', 'code': 'GEL'}],
        'timezones': ['UTC+4'],
        'exports': [
            {'product': 'Agricultural', 'value': 5.2, 'percentage': 32.0},
            {'product': 'Metals', 'value': 4.5, 'percentage': 28.0},
            {'product': 'Other', 'value': 6.3, 'percentage': 40.0}
        ]
    },
    {
        'code': 'IND',
        'name': 'India',
        'capital': 'New Delhi',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 1380000000,
        'area': 3287263,
        'gdp': 3736,
        'languages': ['Hindi', 'English'],
        'currencies': [{'name': 'Indian Rupee', 'symbol': '₹', 'code': 'INR'}],
        'timezones': ['UTC+5:30'],
        'exports': [
            {'product': 'Refined Petroleum', 'value': 85.6, 'percentage': 18.0},
            {'product': 'Pharmaceuticals', 'value': 50.2, 'percentage': 10.5},
            {'product': 'Jewelry', 'value': 45.8, 'percentage': 9.5},
            {'product': 'Vehicles', 'value': 40.3, 'percentage': 8.5},
            {'product': 'Textiles', 'value': 35.6, 'percentage': 7.5},
            {'product': 'Other', 'value': 215.5, 'percentage': 46.0}
        ]
    },
    {
        'code': 'IDN',
        'name': 'Indonesia',
        'capital': 'Jakarta',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 273000000,
        'area': 1904569,
        'gdp': 1328,
        'languages': ['Indonesian'],
        'currencies': [{'name': 'Indonesian Rupiah', 'symbol': 'Rp', 'code': 'IDR'}],
        'timezones': ['UTC+7 to UTC+9'],
        'exports': [
            {'product': 'Palm Oil', 'value': 55.3, 'percentage': 15.0},
            {'product': 'Coal', 'value': 45.2, 'percentage': 12.0},
            {'product': 'Petroleum', 'value': 40.8, 'percentage': 11.0},
            {'product': 'Natural Gas', 'value': 35.4, 'percentage': 9.5},
            {'product': 'Other', 'value': 195.3, 'percentage': 52.5}
        ]
    },
    {
        'code': 'IRN',
        'name': 'Iran',
        'capital': 'Tehran',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 83900000,
        'area': 1648195,
        'gdp': 388,
        'languages': ['Persian'],
        'currencies': [{'name': 'Iranian Rial', 'symbol': '﷼', 'code': 'IRR'}],
        'timezones': ['UTC+3:30'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 80.8, 'percentage': 55.0},
            {'product': 'Petrochemicals', 'value': 30.2, 'percentage': 20.0},
            {'product': 'Other', 'value': 37.0, 'percentage': 25.0}
        ]
    },
    {
        'code': 'IRQ',
        'name': 'Iraq',
        'capital': 'Baghdad',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 40200000,
        'area': 438317,
        'gdp': 282,
        'languages': ['Arabic', 'Kurdish'],
        'currencies': [{'name': 'Iraqi Dinar', 'symbol': 'ع.د', 'code': 'IQD'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 85.8, 'percentage': 90.0},
            {'product': 'Other', 'value': 9.2, 'percentage': 10.0}
        ]
    },
    {
        'code': 'ISR',
        'name': 'Israel',
        'capital': 'Jerusalem',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 8650000,
        'area': 20770,
        'gdp': 520,
        'languages': ['Hebrew', 'Arabic'],
        'currencies': [{'name': 'Israeli Shekel', 'symbol': '₪', 'code': 'ILS'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Electronics', 'value': 45.3, 'percentage': 25.0},
            {'product': 'Pharmaceuticals', 'value': 35.2, 'percentage': 19.0},
            {'product': 'Machinery', 'value': 30.8, 'percentage': 17.0},
            {'product': 'Other', 'value': 70.7, 'percentage': 39.0}
        ]
    },
    {
        'code': 'JPN',
        'name': 'Japan',
        'capital': 'Tokyo',
        'region': 'Asia',
        'subregion': 'Eastern Asia',
        'population': 125800000,
        'area': 377930,
        'gdp': 4912,
        'languages': ['Japanese'],
        'currencies': [{'name': 'Japanese Yen', 'symbol': '¥', 'code': 'JPY'}],
        'timezones': ['UTC+9'],
        'exports': [
            {'product': 'Vehicles', 'value': 180.6, 'percentage': 20.0},
            {'product': 'Electronics', 'value': 150.4, 'percentage': 16.7},
            {'product': 'Machinery', 'value': 140.8, 'percentage': 15.6},
            {'product': 'Optical/Medical', 'value': 110.2, 'percentage': 12.2},
            {'product': 'Chemicals', 'value': 100.5, 'percentage': 11.1},
            {'product': 'Other', 'value': 220.5, 'percentage': 24.4}
        ]
    },
    {
        'code': 'JOR',
        'name': 'Jordan',
        'capital': 'Amman',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 10200000,
        'area': 89342,
        'gdp': 49,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Jordanian Dinar', 'symbol': 'د.ا', 'code': 'JOD'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Pharmaceuticals', 'value': 8.3, 'percentage': 25.0},
            {'product': 'Fertilizers', 'value': 6.2, 'percentage': 19.0},
            {'product': 'Other', 'value': 18.5, 'percentage': 56.0}
        ]
    },
    {
        'code': 'KAZ',
        'name': 'Kazakhstan',
        'capital': 'Nur-Sultan',
        'region': 'Asia',
        'subregion': 'Central Asia',
        'population': 18700000,
        'area': 2724900,
        'gdp': 226,
        'languages': ['Kazakh', 'Russian'],
        'currencies': [{'name': 'Kazakhstani Tenge', 'symbol': '₸', 'code': 'KZT'}],
        'timezones': ['UTC+5'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 45.8, 'percentage': 50.0},
            {'product': 'Metals', 'value': 15.2, 'percentage': 17.0},
            {'product': 'Chemicals', 'value': 10.8, 'percentage': 12.0},
            {'product': 'Other', 'value': 19.2, 'percentage': 21.0}
        ]
    },
    {
        'code': 'KWT',
        'name': 'Kuwait',
        'capital': 'Kuwait City',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 4270000,
        'area': 17818,
        'gdp': 221,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Kuwaiti Dinar', 'symbol': 'د.ك', 'code': 'KWD'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 65.8, 'percentage': 75.0},
            {'product': 'Petrochemicals', 'value': 15.2, 'percentage': 17.0},
            {'product': 'Other', 'value': 7.0, 'percentage': 8.0}
        ]
    },
    {
        'code': 'KGZ',
        'name': 'Kyrgyzstan',
        'capital': 'Bishkek',
        'region': 'Asia',
        'subregion': 'Central Asia',
        'population': 6600000,
        'area': 199951,
        'gdp': 10,
        'languages': ['Kyrgyz', 'Russian'],
        'currencies': [{'name': 'Kyrgyzstani Som', 'symbol': 'с', 'code': 'KGS'}],
        'timezones': ['UTC+6'],
        'exports': [
            {'product': 'Gold', 'value': 3.2, 'percentage': 40.0},
            {'product': 'Agricultural', 'value': 2.5, 'percentage': 31.0},
            {'product': 'Other', 'value': 2.3, 'percentage': 29.0}
        ]
    },
    {
        'code': 'LAO',
        'name': 'Laos',
        'capital': 'Vientiane',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 7300000,
        'area': 236800,
        'gdp': 19,
        'languages': ['Lao'],
        'currencies': [{'name': 'Lao Kip', 'symbol': '₭', 'code': 'LAK'}],
        'timezones': ['UTC+7'],
        'exports': [
            {'product': 'Hydro', 'value': 4.2, 'percentage': 35.0},
            {'product': 'Minerals', 'value': 3.5, 'percentage': 29.0},
            {'product': 'Other', 'value': 4.3, 'percentage': 36.0}
        ]
    },
    {
        'code': 'LBN',
        'name': 'Lebanon',
        'capital': 'Beirut',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 6800000,
        'area': 10452,
        'gdp': 23,
        'languages': ['Arabic', 'French'],
        'currencies': [{'name': 'Lebanese Pound', 'symbol': 'ل.ل', 'code': 'LBP'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Jewelry', 'value': 4.3, 'percentage': 28.0},
            {'product': 'Chemicals', 'value': 3.2, 'percentage': 21.0},
            {'product': 'Other', 'value': 7.5, 'percentage': 51.0}
        ]
    },
    {
        'code': 'MYS',
        'name': 'Malaysia',
        'capital': 'Kuala Lumpur',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 32700000,
        'area': 330803,
        'gdp': 430,
        'languages': ['Malay'],
        'currencies': [{'name': 'Malaysian Ringgit', 'symbol': 'RM', 'code': 'MYR'}],
        'timezones': ['UTC+8'],
        'exports': [
            {'product': 'Electronics', 'value': 65.3, 'percentage': 28.0},
            {'product': 'Palm Oil', 'value': 35.2, 'percentage': 15.0},
            {'product': 'Petroleum', 'value': 30.8, 'percentage': 13.0},
            {'product': 'Other', 'value': 102.7, 'percentage': 44.0}
        ]
    },
    {
        'code': 'MDV',
        'name': 'Maldives',
        'capital': 'Malé',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 540000,
        'area': 298,
        'gdp': 5.8,
        'languages': ['Dhivehi'],
        'currencies': [{'name': 'Maldivian Rufiyaa', 'symbol': 'ރ.', 'code': 'MVR'}],
        'timezones': ['UTC+5'],
        'exports': [
            {'product': 'Tourism', 'value': 3.2, 'percentage': 70.0},
            {'product': 'Fish', 'value': 1.2, 'percentage': 26.0},
            {'product': 'Other', 'value': 0.4, 'percentage': 4.0}
        ]
    },
    {
        'code': 'MNG',
        'name': 'Mongolia',
        'capital': 'Ulaanbaatar',
        'region': 'Asia',
        'subregion': 'Eastern Asia',
        'population': 3300000,
        'area': 1564116,
        'gdp': 17,
        'languages': ['Mongolian'],
        'currencies': [{'name': 'Mongolian Tögrög', 'symbol': '₮', 'code': 'MNT'}],
        'timezones': ['UTC+7 to UTC+8'],
        'exports': [
            {'product': 'Copper', 'value': 6.2, 'percentage': 45.0},
            {'product': 'Coal', 'value': 4.5, 'percentage': 33.0},
            {'product': 'Other', 'value': 3.3, 'percentage': 22.0}
        ]
    },
    {
        'code': 'MMR',
        'name': 'Myanmar',
        'capital': 'Naypyidaw',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 54400000,
        'area': 676578,
        'gdp': 69,
        'languages': ['Burmese'],
        'currencies': [{'name': 'Burmese Kyat', 'symbol': 'Ks', 'code': 'MMK'}],
        'timezones': ['UTC+6:30'],
        'exports': [
            {'product': 'Gas', 'value': 12.2, 'percentage': 32.0},
            {'product': 'Textiles', 'value': 10.5, 'percentage': 28.0},
            {'product': 'Other', 'value': 15.3, 'percentage': 40.0}
        ]
    },
    {
        'code': 'NPL',
        'name': 'Nepal',
        'capital': 'Kathmandu',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 29100000,
        'area': 147181,
        'gdp': 41,
        'languages': ['Nepali'],
        'currencies': [{'name': 'Nepalese Rupee', 'symbol': 'रू', 'code': 'NPR'}],
        'timezones': ['UTC+5:45'],
        'exports': [
            {'product': 'Textiles', 'value': 8.2, 'percentage': 38.0},
            {'product': 'Agricultural', 'value': 6.5, 'percentage': 30.0},
            {'product': 'Other', 'value': 7.3, 'percentage': 32.0}
        ]
    },
    {
        'code': 'PRK',
        'name': 'North Korea',
        'capital': 'Pyongyang',
        'region': 'Asia',
        'subregion': 'Eastern Asia',
        'population': 25700000,
        'area': 120538,
        'gdp': 18,
        'languages': ['Korean'],
        'currencies': [{'name': 'North Korean Won', 'symbol': '₩', 'code': 'KPW'}],
        'timezones': ['UTC+9'],
        'exports': [
            {'product': 'Minerals', 'value': 5.2, 'percentage': 45.0},
            {'product': 'Other', 'value': 6.8, 'percentage': 55.0}
        ]
    },
    {
        'code': 'OMN',
        'name': 'Oman',
        'capital': 'Muscat',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 5110000,
        'area': 309500,
        'gdp': 92,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Omani Rial', 'symbol': 'ر.ع', 'code': 'OMR'}],
        'timezones': ['UTC+4'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 35.8, 'percentage': 55.0},
            {'product': 'Natural Gas', 'value': 15.2, 'percentage': 23.0},
            {'product': 'Other', 'value': 14.0, 'percentage': 22.0}
        ]
    },
    {
        'code': 'PAK',
        'name': 'Pakistan',
        'capital': 'Islamabad',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 220000000,
        'area': 881913,
        'gdp': 376,
        'languages': ['Urdu', 'English'],
        'currencies': [{'name': 'Pakistani Rupee', 'symbol': '₨', 'code': 'PKR'}],
        'timezones': ['UTC+5'],
        'exports': [
            {'product': 'Textiles', 'value': 35.2, 'percentage': 55.0},
            {'product': 'Leather', 'value': 8.5, 'percentage': 13.0},
            {'product': 'Other', 'value': 20.3, 'percentage': 32.0}
        ]
    },
    {
        'code': 'PSE',
        'name': 'Palestine',
        'capital': 'Ramallah',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 5100000,
        'area': 6020,
        'gdp': 18,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Israeli Shekel', 'symbol': '₪', 'code': 'ILS'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Agricultural', 'value': 4.2, 'percentage': 35.0},
            {'product': 'Stone', 'value': 3.5, 'percentage': 29.0},
            {'product': 'Other', 'value': 4.3, 'percentage': 36.0}
        ]
    },
    {
        'code': 'PHL',
        'name': 'Philippines',
        'capital': 'Manila',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 109500000,
        'area': 300000,
        'gdp': 404,
        'languages': ['Filipino', 'English'],
        'currencies': [{'name': 'Philippine Peso', 'symbol': '₱', 'code': 'PHP'}],
        'timezones': ['UTC+8'],
        'exports': [
            {'product': 'Electronics', 'value': 45.3, 'percentage': 30.0},
            {'product': 'Machinery', 'value': 25.2, 'percentage': 17.0},
            {'product': 'Agricultural', 'value': 20.8, 'percentage': 14.0},
            {'product': 'Other', 'value': 57.7, 'percentage': 39.0}
        ]
    },
    {
        'code': 'QAT',
        'name': 'Qatar',
        'capital': 'Doha',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 2800000,
        'area': 11586,
        'gdp': 226,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Qatari Riyal', 'symbol': 'ر.ق', 'code': 'QAR'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Natural Gas', 'value': 85.8, 'percentage': 60.0},
            {'product': 'Petroleum', 'value': 35.2, 'percentage': 25.0},
            {'product': 'Other', 'value': 21.0, 'percentage': 15.0}
        ]
    },
    {
        'code': 'SAU',
        'name': 'Saudi Arabia',
        'capital': 'Riyadh',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 34800000,
        'area': 2149690,
        'gdp': 1040,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Saudi Riyal', 'symbol': '﷼', 'code': 'SAR'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 150.8, 'percentage': 45.0},
            {'product': 'Petrochemicals', 'value': 60.2, 'percentage': 18.0},
            {'product': 'Plastics', 'value': 40.8, 'percentage': 12.0},
            {'product': 'Other', 'value': 83.2, 'percentage': 25.0}
        ]
    },
    {
        'code': 'SGP',
        'name': 'Singapore',
        'capital': 'Singapore',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 5700000,
        'area': 728,
        'gdp': 424,
        'languages': ['English', 'Malay', 'Mandarin', 'Tamil'],
        'currencies': [{'name': 'Singapore Dollar', 'symbol': '$', 'code': 'SGD'}],
        'timezones': ['UTC+8'],
        'exports': [
            {'product': 'Electronics', 'value': 85.3, 'percentage': 30.0},
            {'product': 'Machinery', 'value': 55.2, 'percentage': 19.0},
            {'product': 'Chemicals', 'value': 45.8, 'percentage': 16.0},
            {'product': 'Other', 'value': 99.7, 'percentage': 35.0}
        ]
    },
    {
        'code': 'KOR',
        'name': 'South Korea',
        'capital': 'Seoul',
        'region': 'Asia',
        'subregion': 'Eastern Asia',
        'population': 51700000,
        'area': 100210,
        'gdp': 1810,
        'languages': ['Korean'],
        'currencies': [{'name': 'South Korean Won', 'symbol': '₩', 'code': 'KRW'}],
        'timezones': ['UTC+9'],
        'exports': [
            {'product': 'Electronics', 'value': 200.5, 'percentage': 22.0},
            {'product': 'Vehicles', 'value': 150.3, 'percentage': 16.5},
            {'product': 'Machinery', 'value': 120.8, 'percentage': 13.0},
            {'product': 'Ships', 'value': 100.2, 'percentage': 11.0},
            {'product': 'Other', 'value': 340.2, 'percentage': 37.5}
        ]
    },
    {
        'code': 'LKA',
        'name': 'Sri Lanka',
        'capital': 'Colombo',
        'region': 'Asia',
        'subregion': 'Southern Asia',
        'population': 21400000,
        'area': 65610,
        'gdp': 84,
        'languages': ['Sinhala', 'Tamil'],
        'currencies': [{'name': 'Sri Lankan Rupee', 'symbol': 'රු', 'code': 'LKR'}],
        'timezones': ['UTC+5:30'],
        'exports': [
            {'product': 'Textiles', 'value': 15.2, 'percentage': 42.0},
            {'product': 'Tea', 'value': 8.5, 'percentage': 23.0},
            {'product': 'Other', 'value': 12.3, 'percentage': 35.0}
        ]
    },
    {
        'code': 'SYR',
        'name': 'Syria',
        'capital': 'Damascus',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 17500000,
        'area': 185180,
        'gdp': 22,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Syrian Pound', 'symbol': 'ل.س', 'code': 'SYP'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Oil', 'value': 5.2, 'percentage': 35.0},
            {'product': 'Agricultural', 'value': 4.5, 'percentage': 30.0},
            {'product': 'Other', 'value': 5.3, 'percentage': 35.0}
        ]
    },
    {
        'code': 'TWN',
        'name': 'Taiwan',
        'capital': 'Taipei',
        'region': 'Asia',
        'subregion': 'Eastern Asia',
        'population': 23500000,
        'area': 36193,
        'gdp': 841,
        'languages': ['Mandarin'],
        'currencies': [{'name': 'New Taiwan Dollar', 'symbol': 'NT$', 'code': 'TWD'}],
        'timezones': ['UTC+8'],
        'exports': [
            {'product': 'Electronics', 'value': 120.5, 'percentage': 38.0},
            {'product': 'Machinery', 'value': 65.2, 'percentage': 21.0},
            {'product': 'Chemicals', 'value': 45.8, 'percentage': 14.0},
            {'product': 'Other', 'value': 85.5, 'percentage': 27.0}
        ]
    },
    {
        'code': 'TJK',
        'name': 'Tajikistan',
        'capital': 'Dushanbe',
        'region': 'Asia',
        'subregion': 'Central Asia',
        'population': 9500000,
        'area': 143100,
        'gdp': 10,
        'languages': ['Tajik'],
        'currencies': [{'name': 'Tajikistani Somoni', 'symbol': 'ЅМ', 'code': 'TJS'}],
        'timezones': ['UTC+5'],
        'exports': [
            {'product': 'Aluminum', 'value': 3.2, 'percentage': 45.0},
            {'product': 'Cotton', 'value': 2.5, 'percentage': 35.0},
            {'product': 'Other', 'value': 1.3, 'percentage': 20.0}
        ]
    },
    {
        'code': 'THA',
        'name': 'Thailand',
        'capital': 'Bangkok',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 69800000,
        'area': 513120,
        'gdp': 536,
        'languages': ['Thai'],
        'currencies': [{'name': 'Thai Baht', 'symbol': '฿', 'code': 'THB'}],
        'timezones': ['UTC+7'],
        'exports': [
            {'product': 'Electronics', 'value': 55.3, 'percentage': 20.0},
            {'product': 'Vehicles', 'value': 45.2, 'percentage': 16.0},
            {'product': 'Rubber', 'value': 35.8, 'percentage': 13.0},
            {'product': 'Food', 'value': 30.4, 'percentage': 11.0},
            {'product': 'Other', 'value': 108.3, 'percentage': 40.0}
        ]
    },
    {
        'code': 'TLS',
        'name': 'Timor-Leste',
        'capital': 'Dili',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 1300000,
        'area': 14874,
        'gdp': 2.8,
        'languages': ['Tetum', 'Portuguese'],
        'currencies': [{'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}],
        'timezones': ['UTC+9'],
        'exports': [
            {'product': 'Oil', 'value': 1.2, 'percentage': 65.0},
            {'product': 'Coffee', 'value': 0.5, 'percentage': 27.0},
            {'product': 'Other', 'value': 0.3, 'percentage': 8.0}
        ]
    },
    {
        'code': 'TUR',
        'name': 'Turkey',
        'capital': 'Ankara',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 84300000,
        'area': 783562,
        'gdp': 942,
        'languages': ['Turkish'],
        'currencies': [{'name': 'Turkish Lira', 'symbol': '₺', 'code': 'TRY'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Vehicles', 'value': 55.3, 'percentage': 18.0},
            {'product': 'Machinery', 'value': 45.2, 'percentage': 15.0},
            {'product': 'Textiles', 'value': 40.8, 'percentage': 13.0},
            {'product': 'Other', 'value': 160.7, 'percentage': 54.0}
        ]
    },
    {
        'code': 'TKM',
        'name': 'Turkmenistan',
        'capital': 'Ashgabat',
        'region': 'Asia',
        'subregion': 'Central Asia',
        'population': 6000000,
        'area': 488100,
        'gdp': 76,
        'languages': ['Turkmen'],
        'currencies': [{'name': 'Turkmenistani Manat', 'symbol': 'm', 'code': 'TMT'}],
        'timezones': ['UTC+5'],
        'exports': [
            {'product': 'Natural Gas', 'value': 25.2, 'percentage': 70.0},
            {'product': 'Oil', 'value': 8.5, 'percentage': 24.0},
            {'product': 'Other', 'value': 2.3, 'percentage': 6.0}
        ]
    },
    {
        'code': 'ARE',
        'name': 'United Arab Emirates',
        'capital': 'Abu Dhabi',
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 9890000,
        'area': 83600,
        'gdp': 501,
        'languages': ['Arabic'],
        'currencies': [{'name': 'UAE Dirham', 'symbol': 'د.إ', 'code': 'AED'}],
        'timezones': ['UTC+4'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 85.8, 'percentage': 35.0},
            {'product': 'Gold', 'value': 45.2, 'percentage': 18.0},
            {'product': 'Electronics', 'value': 35.8, 'percentage': 14.0},
            {'product': 'Other', 'value': 84.2, 'percentage': 33.0}
        ]
    },
    {
        'code': 'UZB',
        'name': 'Uzbekistan',
        'capital': 'Tashkent',
        'region': 'Asia',
        'subregion': 'Central Asia',
        'population': 33400000,
        'area': 447400,
        'gdp': 80,
        'languages': ['Uzbek'],
        'currencies': [{'name': 'Uzbekistani Som', 'symbol': 'soʻm', 'code': 'UZS'}],
        'timezones': ['UTC+5'],
        'exports': [
            {'product': 'Gold', 'value': 15.8, 'percentage': 35.0},
            {'product': 'Cotton', 'value': 8.2, 'percentage': 18.0},
            {'product': 'Natural Gas', 'value': 6.8, 'percentage': 15.0},
            {'product': 'Other', 'value': 14.2, 'percentage': 32.0}
        ]
    },
    {
        'code': 'VNM',
        'name': 'Vietnam',
        'capital': 'Hanoi',
        'region': 'Asia',
        'subregion': 'South-Eastern Asia',
        'population': 97300000,
        'area': 331212,
        'gdp': 406,
        'languages': ['Vietnamese'],
        'currencies': [{'name': 'Vietnamese Dong', 'symbol': '₫', 'code': 'VND'}],
        'timezones': ['UTC+7'],
        'exports': [
            {'product': 'Electronics', 'value': 65.3, 'percentage': 25.0},
            {'product': 'Textiles', 'value': 45.2, 'percentage': 17.0},
            {'product': 'Footwear', 'value': 35.8, 'percentage': 14.0},
            {'product': 'Furniture', 'value': 30.4, 'percentage': 12.0},
            {'product': 'Other', 'value': 82.3, 'percentage': 32.0}
        ]
    },
    {
        'code': 'YEM',
        'name': 'Yemen',
        'capital': "Sana'a",
        'region': 'Asia',
        'subregion': 'Western Asia',
        'population': 29800000,
        'area': 527968,
        'gdp': 28,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Yemeni Rial', 'symbol': '﷼', 'code': 'YER'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 8.8, 'percentage': 70.0},
            {'product': 'Other', 'value': 3.2, 'percentage': 30.0}
        ]
    },

    # ==================== AFRICA ====================
    {
        'code': 'DZA',
        'name': 'Algeria',
        'capital': 'Algiers',
        'region': 'Africa',
        'subregion': 'Northern Africa',
        'population': 43800000,
        'area': 2381741,
        'gdp': 191,
        'languages': ['Arabic', 'Berber'],
        'currencies': [{'name': 'Algerian Dinar', 'symbol': 'د.ج', 'code': 'DZD'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 45.8, 'percentage': 65.0},
            {'product': 'Natural Gas', 'value': 20.2, 'percentage': 29.0},
            {'product': 'Other', 'value': 4.0, 'percentage': 6.0}
        ]
    },
    {
        'code': 'AGO',
        'name': 'Angola',
        'capital': 'Luanda',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 32800000,
        'area': 1246700,
        'gdp': 124,
        'languages': ['Portuguese'],
        'currencies': [{'name': 'Angolan Kwanza', 'symbol': 'Kz', 'code': 'AOA'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 55.8, 'percentage': 85.0},
            {'product': 'Diamonds', 'value': 8.2, 'percentage': 12.0},
            {'product': 'Other', 'value': 2.0, 'percentage': 3.0}
        ]
    },
    {
        'code': 'BEN',
        'name': 'Benin',
        'capital': 'Porto-Novo',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 12100000,
        'area': 112622,
        'gdp': 18,
        'languages': ['French'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Cotton', 'value': 4.2, 'percentage': 35.0},
            {'product': 'Agricultural', 'value': 3.5, 'percentage': 29.0},
            {'product': 'Other', 'value': 4.3, 'percentage': 36.0}
        ]
    },
    {
        'code': 'BWA',
        'name': 'Botswana',
        'capital': 'Gaborone',
        'region': 'Africa',
        'subregion': 'Southern Africa',
        'population': 2300000,
        'area': 581730,
        'gdp': 18,
        'languages': ['English', 'Tswana'],
        'currencies': [{'name': 'Botswana Pula', 'symbol': 'P', 'code': 'BWP'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Diamonds', 'value': 8.2, 'percentage': 70.0},
            {'product': 'Other', 'value': 3.8, 'percentage': 30.0}
        ]
    },
    {
        'code': 'BFA',
        'name': 'Burkina Faso',
        'capital': 'Ouagadougou',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 20900000,
        'area': 274200,
        'gdp': 20,
        'languages': ['French'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Gold', 'value': 5.2, 'percentage': 45.0},
            {'product': 'Cotton', 'value': 3.5, 'percentage': 30.0},
            {'product': 'Other', 'value': 3.3, 'percentage': 25.0}
        ]
    },
    {
        'code': 'BDI',
        'name': 'Burundi',
        'capital': 'Gitega',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 11900000,
        'area': 27834,
        'gdp': 3,
        'languages': ['Kirundi', 'French', 'English'],
        'currencies': [{'name': 'Burundian Franc', 'symbol': 'Fr', 'code': 'BIF'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Coffee', 'value': 1.2, 'percentage': 45.0},
            {'product': 'Tea', 'value': 0.5, 'percentage': 19.0},
            {'product': 'Other', 'value': 1.3, 'percentage': 36.0}
        ]
    },
    {
        'code': 'CPV',
        'name': 'Cabo Verde',
        'capital': 'Praia',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 550000,
        'area': 4033,
        'gdp': 2,
        'languages': ['Portuguese'],
        'currencies': [{'name': 'Cape Verdean Escudo', 'symbol': '$', 'code': 'CVE'}],
        'timezones': ['UTC-1'],
        'exports': [
            {'product': 'Services', 'value': 0.8, 'percentage': 55.0},
            {'product': 'Other', 'value': 0.7, 'percentage': 45.0}
        ]
    },
    {
        'code': 'CMR',
        'name': 'Cameroon',
        'capital': 'Yaoundé',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 26500000,
        'area': 475442,
        'gdp': 46,
        'languages': ['French', 'English'],
        'currencies': [{'name': 'Central African CFA Franc', 'symbol': 'FCFA', 'code': 'XAF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Oil', 'value': 8.8, 'percentage': 30.0},
            {'product': 'Wood', 'value': 6.2, 'percentage': 21.0},
            {'product': 'Cocoa', 'value': 5.8, 'percentage': 20.0},
            {'product': 'Other', 'value': 8.2, 'percentage': 29.0}
        ]
    },
    {
        'code': 'CAF',
        'name': 'Central African Republic',
        'capital': 'Bangui',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 4800000,
        'area': 622984,
        'gdp': 3,
        'languages': ['French', 'Sango'],
        'currencies': [{'name': 'Central African CFA Franc', 'symbol': 'FCFA', 'code': 'XAF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Wood', 'value': 1.2, 'percentage': 45.0},
            {'product': 'Diamonds', 'value': 0.8, 'percentage': 30.0},
            {'product': 'Other', 'value': 0.7, 'percentage': 25.0}
        ]
    },
    {
        'code': 'TCD',
        'name': 'Chad',
        'capital': "N'Djamena",
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 16400000,
        'area': 1284000,
        'gdp': 12,
        'languages': ['French', 'Arabic'],
        'currencies': [{'name': 'Central African CFA Franc', 'symbol': 'FCFA', 'code': 'XAF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Oil', 'value': 5.2, 'percentage': 75.0},
            {'product': 'Other', 'value': 1.8, 'percentage': 25.0}
        ]
    },
    {
        'code': 'COM',
        'name': 'Comoros',
        'capital': 'Moroni',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 870000,
        'area': 2235,
        'gdp': 1.2,
        'languages': ['Comorian', 'Arabic', 'French'],
        'currencies': [{'name': 'Comorian Franc', 'symbol': 'Fr', 'code': 'KMF'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Vanilla', 'value': 0.4, 'percentage': 45.0},
            {'product': 'Cloves', 'value': 0.3, 'percentage': 34.0},
            {'product': 'Other', 'value': 0.2, 'percentage': 21.0}
        ]
    },
    {
        'code': 'COD',
        'name': 'Democratic Republic of the Congo',
        'capital': 'Kinshasa',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 89500000,
        'area': 2344858,
        'gdp': 63,
        'languages': ['French'],
        'currencies': [{'name': 'Congolese Franc', 'symbol': 'Fr', 'code': 'CDF'}],
        'timezones': ['UTC+1 to UTC+2'],
        'exports': [
            {'product': 'Copper', 'value': 15.2, 'percentage': 45.0},
            {'product': 'Cobalt', 'value': 10.5, 'percentage': 31.0},
            {'product': 'Other', 'value': 8.3, 'percentage': 24.0}
        ]
    },
    {
        'code': 'COG',
        'name': 'Republic of the Congo',
        'capital': 'Brazzaville',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 5500000,
        'area': 342000,
        'gdp': 14,
        'languages': ['French'],
        'currencies': [{'name': 'Central African CFA Franc', 'symbol': 'FCFA', 'code': 'XAF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Oil', 'value': 8.2, 'percentage': 70.0},
            {'product': 'Wood', 'value': 2.5, 'percentage': 21.0},
            {'product': 'Other', 'value': 1.3, 'percentage': 9.0}
        ]
    },
    {
        'code': 'CIV',
        'name': "Côte d'Ivoire",
        'capital': 'Yamoussoukro',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 26300000,
        'area': 322463,
        'gdp': 73,
        'languages': ['French'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Cocoa', 'value': 18.8, 'percentage': 40.0},
            {'product': 'Gold', 'value': 8.2, 'percentage': 17.0},
            {'product': 'Oil', 'value': 6.8, 'percentage': 14.0},
            {'product': 'Other', 'value': 14.2, 'percentage': 29.0}
        ]
    },
    {
        'code': 'DJI',
        'name': 'Djibouti',
        'capital': 'Djibouti',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 990000,
        'area': 23200,
        'gdp': 3.5,
        'languages': ['Arabic', 'French'],
        'currencies': [{'name': 'Djiboutian Franc', 'symbol': 'Fr', 'code': 'DJF'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Services', 'value': 1.2, 'percentage': 55.0},
            {'product': 'Other', 'value': 1.0, 'percentage': 45.0}
        ]
    },
    {
        'code': 'EGY',
        'name': 'Egypt',
        'capital': 'Cairo',
        'region': 'Africa',
        'subregion': 'Northern Africa',
        'population': 102000000,
        'area': 1002450,
        'gdp': 476,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Egyptian Pound', 'symbol': '£', 'code': 'EGP'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 35.8, 'percentage': 22.0},
            {'product': 'Natural Gas', 'value': 25.2, 'percentage': 15.0},
            {'product': 'Textiles', 'value': 20.8, 'percentage': 13.0},
            {'product': 'Agricultural', 'value': 18.4, 'percentage': 11.0},
            {'product': 'Other', 'value': 63.8, 'percentage': 39.0}
        ]
    },
    {
        'code': 'GNQ',
        'name': 'Equatorial Guinea',
        'capital': 'Malabo',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 1400000,
        'area': 28051,
        'gdp': 12,
        'languages': ['Spanish', 'French', 'Portuguese'],
        'currencies': [{'name': 'Central African CFA Franc', 'symbol': 'FCFA', 'code': 'XAF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Oil & Gas', 'value': 8.2, 'percentage': 85.0},
            {'product': 'Other', 'value': 1.8, 'percentage': 15.0}
        ]
    },
    {
        'code': 'ERI',
        'name': 'Eritrea',
        'capital': 'Asmara',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 3500000,
        'area': 117600,
        'gdp': 2.1,
        'languages': ['Tigrinya', 'Arabic', 'English'],
        'currencies': [{'name': 'Eritrean Nakfa', 'symbol': 'Nfk', 'code': 'ERN'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Minerals', 'value': 0.8, 'percentage': 45.0},
            {'product': 'Other', 'value': 1.0, 'percentage': 55.0}
        ]
    },
    {
        'code': 'SWZ',
        'name': 'Eswatini',
        'capital': 'Mbabane',
        'region': 'Africa',
        'subregion': 'Southern Africa',
        'population': 1160000,
        'area': 17364,
        'gdp': 5.2,
        'languages': ['Swazi', 'English'],
        'currencies': [{'name': 'Swazi Lilangeni', 'symbol': 'L', 'code': 'SZL'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Agricultural', 'value': 1.8, 'percentage': 45.0},
            {'product': 'Other', 'value': 2.2, 'percentage': 55.0}
        ]
    },
    {
        'code': 'ETH',
        'name': 'Ethiopia',
        'capital': 'Addis Ababa',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 115000000,
        'area': 1104300,
        'gdp': 126,
        'languages': ['Amharic'],
        'currencies': [{'name': 'Ethiopian Birr', 'symbol': 'Br', 'code': 'ETB'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Coffee', 'value': 15.8, 'percentage': 30.0},
            {'product': 'Gold', 'value': 8.2, 'percentage': 16.0},
            {'product': 'Textiles', 'value': 6.8, 'percentage': 13.0},
            {'product': 'Other', 'value': 21.2, 'percentage': 41.0}
        ]
    },
    {
        'code': 'GAB',
        'name': 'Gabon',
        'capital': 'Libreville',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 2200000,
        'area': 267668,
        'gdp': 20,
        'languages': ['French'],
        'currencies': [{'name': 'Central African CFA Franc', 'symbol': 'FCFA', 'code': 'XAF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Oil', 'value': 8.2, 'percentage': 55.0},
            {'product': 'Manganese', 'value': 3.5, 'percentage': 23.0},
            {'product': 'Wood', 'value': 2.8, 'percentage': 19.0},
            {'product': 'Other', 'value': 0.5, 'percentage': 3.0}
        ]
    },
    {
        'code': 'GMB',
        'name': 'Gambia',
        'capital': 'Banjul',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 2400000,
        'area': 10689,
        'gdp': 2,
        'languages': ['English'],
        'currencies': [{'name': 'Gambian Dalasi', 'symbol': 'D', 'code': 'GMD'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Agricultural', 'value': 0.8, 'percentage': 45.0},
            {'product': 'Other', 'value': 1.0, 'percentage': 55.0}
        ]
    },
    {
        'code': 'GHA',
        'name': 'Ghana',
        'capital': 'Accra',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 31000000,
        'area': 238533,
        'gdp': 77,
        'languages': ['English'],
        'currencies': [{'name': 'Ghanaian Cedi', 'symbol': '₵', 'code': 'GHS'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Gold', 'value': 15.8, 'percentage': 35.0},
            {'product': 'Cocoa', 'value': 10.2, 'percentage': 22.0},
            {'product': 'Oil', 'value': 8.8, 'percentage': 19.0},
            {'product': 'Other', 'value': 11.2, 'percentage': 24.0}
        ]
    },
    {
        'code': 'GIN',
        'name': 'Guinea',
        'capital': 'Conakry',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 13100000,
        'area': 245857,
        'gdp': 18,
        'languages': ['French'],
        'currencies': [{'name': 'Guinean Franc', 'symbol': 'Fr', 'code': 'GNF'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Bauxite', 'value': 5.2, 'percentage': 50.0},
            {'product': 'Gold', 'value': 3.5, 'percentage': 34.0},
            {'product': 'Other', 'value': 1.3, 'percentage': 16.0}
        ]
    },
    {
        'code': 'GNB',
        'name': 'Guinea-Bissau',
        'capital': 'Bissau',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 2000000,
        'area': 36125,
        'gdp': 1.6,
        'languages': ['Portuguese'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Cashew', 'value': 0.8, 'percentage': 65.0},
            {'product': 'Other', 'value': 0.5, 'percentage': 35.0}
        ]
    },
    {
        'code': 'KEN',
        'name': 'Kenya',
        'capital': 'Nairobi',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 53700000,
        'area': 580367,
        'gdp': 114,
        'languages': ['Swahili', 'English'],
        'currencies': [{'name': 'Kenyan Shilling', 'symbol': 'KSh', 'code': 'KES'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Tea', 'value': 12.8, 'percentage': 25.0},
            {'product': 'Horticulture', 'value': 10.2, 'percentage': 20.0},
            {'product': 'Coffee', 'value': 8.8, 'percentage': 17.0},
            {'product': 'Other', 'value': 19.2, 'percentage': 38.0}
        ]
    },
    {
        'code': 'LSO',
        'name': 'Lesotho',
        'capital': 'Maseru',
        'region': 'Africa',
        'subregion': 'Southern Africa',
        'population': 2100000,
        'area': 30355,
        'gdp': 2.5,
        'languages': ['Sesotho', 'English'],
        'currencies': [{'name': 'Lesotho Loti', 'symbol': 'L', 'code': 'LSL'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Textiles', 'value': 0.8, 'percentage': 45.0},
            {'product': 'Other', 'value': 1.0, 'percentage': 55.0}
        ]
    },
    {
        'code': 'LBR',
        'name': 'Liberia',
        'capital': 'Monrovia',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 5100000,
        'area': 111369,
        'gdp': 4,
        'languages': ['English'],
        'currencies': [{'name': 'Liberian Dollar', 'symbol': '$', 'code': 'LRD'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Iron Ore', 'value': 1.2, 'percentage': 40.0},
            {'product': 'Rubber', 'value': 1.0, 'percentage': 33.0},
            {'product': 'Other', 'value': 0.8, 'percentage': 27.0}
        ]
    },
    {
        'code': 'LBY',
        'name': 'Libya',
        'capital': 'Tripoli',
        'region': 'Africa',
        'subregion': 'Northern Africa',
        'population': 6870000,
        'area': 1759540,
        'gdp': 40,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Libyan Dinar', 'symbol': 'ل.د', 'code': 'LYD'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 25.8, 'percentage': 90.0},
            {'product': 'Other', 'value': 3.2, 'percentage': 10.0}
        ]
    },
    {
        'code': 'MDG',
        'name': 'Madagascar',
        'capital': 'Antananarivo',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 27600000,
        'area': 587041,
        'gdp': 14,
        'languages': ['Malagasy', 'French'],
        'currencies': [{'name': 'Malagasy Ariary', 'symbol': 'Ar', 'code': 'MGA'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Vanilla', 'value': 3.2, 'percentage': 28.0},
            {'product': 'Textiles', 'value': 2.8, 'percentage': 24.0},
            {'product': 'Other', 'value': 5.0, 'percentage': 48.0}
        ]
    },
    {
        'code': 'MWI',
        'name': 'Malawi',
        'capital': 'Lilongwe',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 19100000,
        'area': 118484,
        'gdp': 12,
        'languages': ['English', 'Chichewa'],
        'currencies': [{'name': 'Malawian Kwacha', 'symbol': 'MK', 'code': 'MWK'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Tobacco', 'value': 3.2, 'percentage': 45.0},
            {'product': 'Tea', 'value': 1.5, 'percentage': 21.0},
            {'product': 'Other', 'value': 2.3, 'percentage': 34.0}
        ]
    },
    {
        'code': 'MLI',
        'name': 'Mali',
        'capital': 'Bamako',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 20200000,
        'area': 1240192,
        'gdp': 19,
        'languages': ['French'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Gold', 'value': 6.2, 'percentage': 55.0},
            {'product': 'Cotton', 'value': 3.5, 'percentage': 31.0},
            {'product': 'Other', 'value': 1.3, 'percentage': 14.0}
        ]
    },
    {
        'code': 'MRT',
        'name': 'Mauritania',
        'capital': 'Nouakchott',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 4600000,
        'area': 1030700,
        'gdp': 9,
        'languages': ['Arabic'],
        'currencies': [{'name': 'Mauritanian Ouguiya', 'symbol': 'UM', 'code': 'MRU'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Iron Ore', 'value': 3.2, 'percentage': 48.0},
            {'product': 'Fish', 'value': 2.5, 'percentage': 37.0},
            {'product': 'Other', 'value': 1.3, 'percentage': 15.0}
        ]
    },
    {
        'code': 'MUS',
        'name': 'Mauritius',
        'capital': 'Port Louis',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 1270000,
        'area': 2040,
        'gdp': 12,
        'languages': ['English', 'French'],
        'currencies': [{'name': 'Mauritian Rupee', 'symbol': '₨', 'code': 'MUR'}],
        'timezones': ['UTC+4'],
        'exports': [
            {'product': 'Textiles', 'value': 3.2, 'percentage': 32.0},
            {'product': 'Services', 'value': 2.8, 'percentage': 28.0},
            {'product': 'Other', 'value': 4.0, 'percentage': 40.0}
        ]
    },
    {
        'code': 'MAR',
        'name': 'Morocco',
        'capital': 'Rabat',
        'region': 'Africa',
        'subregion': 'Northern Africa',
        'population': 36900000,
        'area': 446550,
        'gdp': 138,
        'languages': ['Arabic', 'Berber'],
        'currencies': [{'name': 'Moroccan Dirham', 'symbol': 'د.م.', 'code': 'MAD'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Vehicles', 'value': 25.8, 'percentage': 25.0},
            {'product': 'Agricultural', 'value': 20.2, 'percentage': 20.0},
            {'product': 'Textiles', 'value': 15.8, 'percentage': 15.0},
            {'product': 'Other', 'value': 41.2, 'percentage': 40.0}
        ]
    },
    {
        'code': 'MOZ',
        'name': 'Mozambique',
        'capital': 'Maputo',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 31200000,
        'area': 801590,
        'gdp': 17,
        'languages': ['Portuguese'],
        'currencies': [{'name': 'Mozambican Metical', 'symbol': 'MT', 'code': 'MZN'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Aluminum', 'value': 4.2, 'percentage': 35.0},
            {'product': 'Coal', 'value': 3.5, 'percentage': 29.0},
            {'product': 'Other', 'value': 4.3, 'percentage': 36.0}
        ]
    },
    {
        'code': 'NAM',
        'name': 'Namibia',
        'capital': 'Windhoek',
        'region': 'Africa',
        'subregion': 'Southern Africa',
        'population': 2500000,
        'area': 824292,
        'gdp': 12,
        'languages': ['English'],
        'currencies': [{'name': 'Namibian Dollar', 'symbol': '$', 'code': 'NAD'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Diamonds', 'value': 3.2, 'percentage': 32.0},
            {'product': 'Uranium', 'value': 2.8, 'percentage': 28.0},
            {'product': 'Other', 'value': 4.0, 'percentage': 40.0}
        ]
    },
    {
        'code': 'NER',
        'name': 'Niger',
        'capital': 'Niamey',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 24200000,
        'area': 1267000,
        'gdp': 15,
        'languages': ['French'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Uranium', 'value': 4.2, 'percentage': 45.0},
            {'product': 'Gold', 'value': 2.5, 'percentage': 27.0},
            {'product': 'Other', 'value': 2.3, 'percentage': 28.0}
        ]
    },
    {
        'code': 'NGA',
        'name': 'Nigeria',
        'capital': 'Abuja',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 206000000,
        'area': 923768,
        'gdp': 504,
        'languages': ['English'],
        'currencies': [{'name': 'Nigerian Naira', 'symbol': '₦', 'code': 'NGN'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Crude Petroleum', 'value': 85.8, 'percentage': 70.0},
            {'product': 'Natural Gas', 'value': 15.2, 'percentage': 12.0},
            {'product': 'Other', 'value': 22.0, 'percentage': 18.0}
        ]
    },
    {
        'code': 'RWA',
        'name': 'Rwanda',
        'capital': 'Kigali',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 12900000,
        'area': 26338,
        'gdp': 12,
        'languages': ['Kinyarwanda', 'French', 'English'],
        'currencies': [{'name': 'Rwandan Franc', 'symbol': 'Fr', 'code': 'RWF'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Gold', 'value': 3.2, 'percentage': 35.0},
            {'product': 'Coffee', 'value': 2.5, 'percentage': 27.0},
            {'product': 'Other', 'value': 3.3, 'percentage': 38.0}
        ]
    },
    {
        'code': 'STP',
        'name': 'São Tomé and Príncipe',
        'capital': 'São Tomé',
        'region': 'Africa',
        'subregion': 'Middle Africa',
        'population': 220000,
        'area': 964,
        'gdp': 0.5,
        'languages': ['Portuguese'],
        'currencies': [{'name': 'São Tomé and Príncipe Dobra', 'symbol': 'Db', 'code': 'STN'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Cocoa', 'value': 0.2, 'percentage': 55.0},
            {'product': 'Other', 'value': 0.1, 'percentage': 45.0}
        ]
    },
    {
        'code': 'SEN',
        'name': 'Senegal',
        'capital': 'Dakar',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 16700000,
        'area': 196722,
        'gdp': 28,
        'languages': ['French'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Gold', 'value': 5.8, 'percentage': 28.0},
            {'product': 'Fish', 'value': 4.2, 'percentage': 20.0},
            {'product': 'Other', 'value': 11.0, 'percentage': 52.0}
        ]
    },
    {
        'code': 'SYC',
        'name': 'Seychelles',
        'capital': 'Victoria',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 98000,
        'area': 455,
        'gdp': 1.8,
        'languages': ['Seychellois Creole', 'English', 'French'],
        'currencies': [{'name': 'Seychellois Rupee', 'symbol': '₨', 'code': 'SCR'}],
        'timezones': ['UTC+4'],
        'exports': [
            {'product': 'Fish', 'value': 0.6, 'percentage': 45.0},
            {'product': 'Services', 'value': 0.5, 'percentage': 38.0},
            {'product': 'Other', 'value': 0.2, 'percentage': 17.0}
        ]
    },
    {
        'code': 'SLE',
        'name': 'Sierra Leone',
        'capital': 'Freetown',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 8000000,
        'area': 71740,
        'gdp': 4,
        'languages': ['English'],
        'currencies': [{'name': 'Sierra Leonean Leone', 'symbol': 'Le', 'code': 'SLL'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Diamonds', 'value': 1.2, 'percentage': 38.0},
            {'product': 'Iron Ore', 'value': 1.0, 'percentage': 32.0},
            {'product': 'Other', 'value': 1.0, 'percentage': 30.0}
        ]
    },
    {
        'code': 'SOM',
        'name': 'Somalia',
        'capital': 'Mogadishu',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 15800000,
        'area': 637657,
        'gdp': 8,
        'languages': ['Somali', 'Arabic'],
        'currencies': [{'name': 'Somali Shilling', 'symbol': 'Sh', 'code': 'SOS'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Livestock', 'value': 2.2, 'percentage': 45.0},
            {'product': 'Bananas', 'value': 1.5, 'percentage': 31.0},
            {'product': 'Other', 'value': 1.3, 'percentage': 24.0}
        ]
    },
    {
        'code': 'ZAF',
        'name': 'South Africa',
        'capital': 'Pretoria',
        'region': 'Africa',
        'subregion': 'Southern Africa',
        'population': 59300000,
        'area': 1221037,
        'gdp': 426,
        'languages': ['Afrikaans', 'English', 'Zulu', 'Xhosa', 'Southern Sotho', 'Tswana', 'Northern Sotho', 'Tsonga', 'Swazi', 'Venda', 'Southern Ndebele'],
        'currencies': [{'name': 'South African Rand', 'symbol': 'R', 'code': 'ZAR'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Gold', 'value': 35.8, 'percentage': 18.0},
            {'product': 'Platinum', 'value': 30.2, 'percentage': 15.0},
            {'product': 'Coal', 'value': 25.8, 'percentage': 13.0},
            {'product': 'Iron Ore', 'value': 20.4, 'percentage': 10.0},
            {'product': 'Other', 'value': 88.8, 'percentage': 44.0}
        ]
    },
    {
        'code': 'SSD',
        'name': 'South Sudan',
        'capital': 'Juba',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 11200000,
        'area': 644329,
        'gdp': 4,
        'languages': ['English'],
        'currencies': [{'name': 'South Sudanese Pound', 'symbol': '£', 'code': 'SSP'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Oil', 'value': 2.2, 'percentage': 85.0},
            {'product': 'Other', 'value': 0.8, 'percentage': 15.0}
        ]
    },
    {
        'code': 'SDN',
        'name': 'Sudan',
        'capital': 'Khartoum',
        'region': 'Africa',
        'subregion': 'Northern Africa',
        'population': 43800000,
        'area': 1861484,
        'gdp': 41,
        'languages': ['Arabic', 'English'],
        'currencies': [{'name': 'Sudanese Pound', 'symbol': '£', 'code': 'SDG'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Gold', 'value': 8.8, 'percentage': 35.0},
            {'product': 'Agricultural', 'value': 6.2, 'percentage': 25.0},
            {'product': 'Other', 'value': 10.0, 'percentage': 40.0}
        ]
    },
    {
        'code': 'TZA',
        'name': 'Tanzania',
        'capital': 'Dodoma',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 59700000,
        'area': 947300,
        'gdp': 77,
        'languages': ['Swahili', 'English'],
        'currencies': [{'name': 'Tanzanian Shilling', 'symbol': 'TSh', 'code': 'TZS'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Gold', 'value': 12.8, 'percentage': 30.0},
            {'product': 'Agricultural', 'value': 8.2, 'percentage': 19.0},
            {'product': 'Other', 'value': 22.0, 'percentage': 51.0}
        ]
    },
    {
        'code': 'TGO',
        'name': 'Togo',
        'capital': 'Lomé',
        'region': 'Africa',
        'subregion': 'Western Africa',
        'population': 8300000,
        'area': 56785,
        'gdp': 8,
        'languages': ['French'],
        'currencies': [{'name': 'West African CFA Franc', 'symbol': 'CFA', 'code': 'XOF'}],
        'timezones': ['UTC+0'],
        'exports': [
            {'product': 'Phosphates', 'value': 2.2, 'percentage': 38.0},
            {'product': 'Cotton', 'value': 1.8, 'percentage': 31.0},
            {'product': 'Other', 'value': 2.0, 'percentage': 31.0}
        ]
    },
    {
        'code': 'TUN',
        'name': 'Tunisia',
        'capital': 'Tunis',
        'region': 'Africa',
        'subregion': 'Northern Africa',
        'population': 11800000,
        'area': 163610,
        'gdp': 47,
        'languages': ['Arabic', 'French'],
        'currencies': [{'name': 'Tunisian Dinar', 'symbol': 'د.ت', 'code': 'TND'}],
        'timezones': ['UTC+1'],
        'exports': [
            {'product': 'Textiles', 'value': 8.8, 'percentage': 25.0},
            {'product': 'Vehicles', 'value': 7.2, 'percentage': 20.0},
            {'product': 'Electrical', 'value': 6.8, 'percentage': 19.0},
            {'product': 'Other', 'value': 13.2, 'percentage': 36.0}
        ]
    },
    {
        'code': 'UGA',
        'name': 'Uganda',
        'capital': 'Kampala',
        'region': 'Africa',
        'subregion': 'Eastern Africa',
        'population': 45700000,
        'area': 241038,
        'gdp': 46,
        'languages': ['English', 'Swahili'],
        'currencies': [{'name': 'Ugandan Shilling', 'symbol': 'USh', 'code': 'UGX'}],
        'timezones': ['UTC+3'],
        'exports': [
            {'product': 'Coffee', 'value': 8.8, 'percentage': 35.0},
            {'product': 'Gold', 'value': 5.2, 'percentage': 21.0},
            {'product': 'Other', 'value': 11.0, 'percentage': 44.0}
        ]
    },
    {
        'code': 'ZMB',
        'name': 'Zambia',
        'capital': 'Lusaka',
        'region': 'Africa',
        'subregion': 'Southern Africa',
        'population': 18300000,
        'area': 752612,
        'gdp': 25,
        'languages': ['English'],
        'currencies': [{'name': 'Zambian Kwacha', 'symbol': 'ZK', 'code': 'ZMW'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Copper', 'value': 12.8, 'percentage': 65.0},
            {'product': 'Cobalt', 'value': 3.2, 'percentage': 16.0},
            {'product': 'Other', 'value': 4.0, 'percentage': 19.0}
        ]
    },
    {
        'code': 'ZWE',
        'name': 'Zimbabwe',
        'capital': 'Harare',
        'region': 'Africa',
        'subregion': 'Southern Africa',
        'population': 14800000,
        'area': 390757,
        'gdp': 36,
        'languages': ['English', 'Shona', 'Northern Ndebele'],
        'currencies': [{'name': 'Zimbabwean Gold', 'symbol': 'ZiG', 'code': 'ZWG'}],
        'timezones': ['UTC+2'],
        'exports': [
            {'product': 'Gold', 'value': 8.8, 'percentage': 35.0},
            {'product': 'Tobacco', 'value': 6.2, 'percentage': 25.0},
            {'product': 'Other', 'value': 10.0, 'percentage': 40.0}
        ]
    },

    # ==================== OCEANIA ====================
    {
        'code': 'AUS',
        'name': 'Australia',
        'capital': 'Canberra',
        'region': 'Oceania',
        'subregion': 'Australia and New Zealand',
        'population': 25700000,
        'area': 7692024,
        'gdp': 1695,
        'languages': ['English'],
        'currencies': [{'name': 'Australian Dollar', 'symbol': '$', 'code': 'AUD'}],
        'timezones': ['UTC+8 to UTC+11'],
        'exports': [
            {'product': 'Iron Ore', 'value': 150.6, 'percentage': 25.0},
            {'product': 'Coal', 'value': 120.4, 'percentage': 20.0},
            {'product': 'Natural Gas', 'value': 90.2, 'percentage': 15.0},
            {'product': 'Gold', 'value': 50.8, 'percentage': 8.5},
            {'product': 'Other', 'value': 190.0, 'percentage': 31.5}
        ]
    },
    {
        'code': 'FJI',
        'name': 'Fiji',
        'capital': 'Suva',
        'region': 'Oceania',
        'subregion': 'Melanesia',
        'population': 890000,
        'area': 18274,
        'gdp': 5.5,
        'languages': ['English', 'Fijian', 'Fiji Hindi'],
        'currencies': [{'name': 'Fijian Dollar', 'symbol': '$', 'code': 'FJD'}],
        'timezones': ['UTC+12'],
        'exports': [
            {'product': 'Water', 'value': 1.2, 'percentage': 25.0},
            {'product': 'Sugar', 'value': 1.1, 'percentage': 23.0},
            {'product': 'Tourism', 'value': 1.0, 'percentage': 21.0},
            {'product': 'Other', 'value': 1.5, 'percentage': 31.0}
        ]
    },
    {
        'code': 'KIR',
        'name': 'Kiribati',
        'capital': 'South Tarawa',
        'region': 'Oceania',
        'subregion': 'Micronesia',
        'population': 120000,
        'area': 811,
        'gdp': 0.2,
        'languages': ['English', 'Gilbertese'],
        'currencies': [{'name': 'Australian Dollar', 'symbol': '$', 'code': 'AUD'}],
        'timezones': ['UTC+12 to UTC+14'],
        'exports': [
            {'product': 'Fish', 'value': 0.1, 'percentage': 55.0},
            {'product': 'Other', 'value': 0.1, 'percentage': 45.0}
        ]
    },
    {
        'code': 'MHL',
        'name': 'Marshall Islands',
        'capital': 'Majuro',
        'region': 'Oceania',
        'subregion': 'Micronesia',
        'population': 59000,
        'area': 181,
        'gdp': 0.2,
        'languages': ['Marshallese', 'English'],
        'currencies': [{'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}],
        'timezones': ['UTC+12'],
        'exports': [
            {'product': 'Services', 'value': 0.1, 'percentage': 60.0},
            {'product': 'Other', 'value': 0.1, 'percentage': 40.0}
        ]
    },
    {
        'code': 'FSM',
        'name': 'Micronesia',
        'capital': 'Palikir',
        'region': 'Oceania',
        'subregion': 'Micronesia',
        'population': 115000,
        'area': 702,
        'gdp': 0.4,
        'languages': ['English'],
        'currencies': [{'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}],
        'timezones': ['UTC+10 to UTC+11'],
        'exports': [
            {'product': 'Fish', 'value': 0.2, 'percentage': 55.0},
            {'product': 'Other', 'value': 0.1, 'percentage': 45.0}
        ]
    },
    {
        'code': 'NRU',
        'name': 'Nauru',
        'capital': 'Yaren',
        'region': 'Oceania',
        'subregion': 'Micronesia',
        'population': 11000,
        'area': 21,
        'gdp': 0.1,
        'languages': ['Nauruan', 'English'],
        'currencies': [{'name': 'Australian Dollar', 'symbol': '$', 'code': 'AUD'}],
        'timezones': ['UTC+12'],
        'exports': [
            {'product': 'Phosphates', 'value': 0.05, 'percentage': 65.0},
            {'product': 'Other', 'value': 0.03, 'percentage': 35.0}
        ]
    },
    {
        'code': 'NZL',
        'name': 'New Zealand',
        'capital': 'Wellington',
        'region': 'Oceania',
        'subregion': 'Australia and New Zealand',
        'population': 5100000,
        'area': 268838,
        'gdp': 248,
        'languages': ['English', 'Māori'],
        'currencies': [{'name': 'New Zealand Dollar', 'symbol': '$', 'code': 'NZD'}],
        'timezones': ['UTC+12'],
        'exports': [
            {'product': 'Dairy', 'value': 45.3, 'percentage': 28.0},
            {'product': 'Meat', 'value': 30.2, 'percentage': 19.0},
            {'product': 'Wood', 'value': 20.8, 'percentage': 13.0},
            {'product': 'Fruit', 'value': 15.4, 'percentage': 9.5},
            {'product': 'Other', 'value': 49.3, 'percentage': 30.5}
        ]
    },
    {
        'code': 'PLW',
        'name': 'Palau',
        'capital': 'Ngerulmud',
        'region': 'Oceania',
        'subregion': 'Micronesia',
        'population': 18000,
        'area': 459,
        'gdp': 0.3,
        'languages': ['Palauan', 'English'],
        'currencies': [{'name': 'US Dollar', 'symbol': '$', 'code': 'USD'}],
        'timezones': ['UTC+9'],
        'exports': [
            {'product': 'Tourism', 'value': 0.15, 'percentage': 60.0},
            {'product': 'Fish', 'value': 0.1, 'percentage': 40.0}
        ]
    },
    {
        'code': 'PNG',
        'name': 'Papua New Guinea',
        'capital': 'Port Moresby',
        'region': 'Oceania',
        'subregion': 'Melanesia',
        'population': 8900000,
        'area': 462840,
        'gdp': 31,
        'languages': ['English', 'Tok Pisin', 'Hiri Motu'],
        'currencies': [{'name': 'Papua New Guinean Kina', 'symbol': 'K', 'code': 'PGK'}],
        'timezones': ['UTC+10'],
        'exports': [
            {'product': 'Gold', 'value': 8.3, 'percentage': 30.0},
            {'product': 'Copper', 'value': 6.2, 'percentage': 22.0},
            {'product': 'Oil', 'value': 5.8, 'percentage': 21.0},
            {'product': 'Other', 'value': 7.7, 'percentage': 27.0}
        ]
    },
    {
        'code': 'WSM',
        'name': 'Samoa',
        'capital': 'Apia',
        'region': 'Oceania',
        'subregion': 'Polynesia',
        'population': 200000,
        'area': 2842,
        'gdp': 0.8,
        'languages': ['Samoan', 'English'],
        'currencies': [{'name': 'Samoan Tala', 'symbol': 'T', 'code': 'WST'}],
        'timezones': ['UTC+13'],
        'exports': [
            {'product': 'Fish', 'value': 0.3, 'percentage': 42.0},
            {'product': 'Agricultural', 'value': 0.2, 'percentage': 28.0},
            {'product': 'Other', 'value': 0.2, 'percentage': 30.0}
        ]
    },
    {
        'code': 'SLB',
        'name': 'Solomon Islands',
        'capital': 'Honiara',
        'region': 'Oceania',
        'subregion': 'Melanesia',
        'population': 700000,
        'area': 28896,
        'gdp': 1.6,
        'languages': ['English'],
        'currencies': [{'name': 'Solomon Islands Dollar', 'symbol': '$', 'code': 'SBD'}],
        'timezones': ['UTC+11'],
        'exports': [
            {'product': 'Wood', 'value': 0.6, 'percentage': 48.0},
            {'product': 'Fish', 'value': 0.4, 'percentage': 32.0},
            {'product': 'Other', 'value': 0.2, 'percentage': 20.0}
        ]
    },
    {
        'code': 'TON',
        'name': 'Tonga',
        'capital': "Nuku'alofa",
        'region': 'Oceania',
        'subregion': 'Polynesia',
        'population': 106000,
        'area': 747,
        'gdp': 0.5,
        'languages': ['Tongan', 'English'],
        'currencies': [{'name': 'Tongan Paʻanga', 'symbol': 'T$', 'code': 'TOP'}],
        'timezones': ['UTC+13'],
        'exports': [
            {'product': 'Agricultural', 'value': 0.2, 'percentage': 45.0},
            {'product': 'Fish', 'value': 0.15, 'percentage': 34.0},
            {'product': 'Other', 'value': 0.1, 'percentage': 21.0}
        ]
    },
    {
        'code': 'TUV',
        'name': 'Tuvalu',
        'capital': 'Funafuti',
        'region': 'Oceania',
        'subregion': 'Polynesia',
        'population': 12000,
        'area': 26,
        'gdp': 0.06,
        'languages': ['Tuvaluan', 'English'],
        'currencies': [{'name': 'Australian Dollar', 'symbol': '$', 'code': 'AUD'}],
        'timezones': ['UTC+12'],
        'exports': [
            {'product': 'Fish', 'value': 0.02, 'percentage': 55.0},
            {'product': 'Other', 'value': 0.02, 'percentage': 45.0}
        ]
    },
    {
        'code': 'VUT',
        'name': 'Vanuatu',
        'capital': 'Port Vila',
        'region': 'Oceania',
        'subregion': 'Melanesia',
        'population': 307000,
        'area': 12189,
        'gdp': 1.0,
        'languages': ['Bislama', 'English', 'French'],
        'currencies': [{'name': 'Vanuatu Vatu', 'symbol': 'Vt', 'code': 'VUV'}],
        'timezones': ['UTC+11'],
        'exports': [
            {'product': 'Agricultural', 'value': 0.4, 'percentage': 48.0},
            {'product': 'Fish', 'value': 0.3, 'percentage': 36.0},
            {'product': 'Other', 'value': 0.1, 'percentage': 16.0}
        ]
    }
]

def get_all_countries():
    """Return all countries"""
    return COUNTRIES

def get_country_by_code(code):
    """Get a country by its ISO3 code"""
    for country in COUNTRIES:
        if country['code'] == code:
            return country
    return None

def search_countries(query):
    """Search countries by name or code"""
    query = query.lower()
    results = []
    for country in COUNTRIES:
        if query in country['name'].lower() or query in country['code'].lower():
            results.append(country)
    return results