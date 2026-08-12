import pandas as pd
from wow_spec_specs import initialize_spec_objects

# Print the first 5 rows of the DataFrame
#print(df.head())
name = '*Item'
catagory = 'Dungeon'
itemtype = '*Slot'
armor_tier = 'Type'
catagory_mainstat = 'Main Stat'
vault_sum = 'Vault'
sanity_checker = 0

#shortened_dungeons = ['Brackenhide', 'Halls of Inf.', 'Neltharus', 'Uldaman', 'Freehold', "Nelth's Lair", 'Underrot', 'Vortex Pin.']
shortened_dungeons = ['BH', 'HoI', 'Nel', 'Ul', 'Fh', "NL", 'TU', 'VP']
shortened_raidboss = ['Kaz', 'Ama', 'Zaq', 'Exp', 'Ras', 'Zsk', 'Mag', 'Nel', 'Sar']
raidboss_order = ['Kazzara', 'Amalgamation', 'Zaqali', 'Experiments', 'Rashok', 'Zskarn', 'Magmorax', 'Neltharion', 'Sarkareth']

#%%

def matching_main_stat(trinket_mainstat, primary_stat):
    return (primary_stat in trinket_mainstat)


def loot_type_compatibility(armor_type, slot, mainstat, instance):
    # Check if cloth/leather/mail/plate
    lst_of_armor_tiers = ['cloth', 'leather', 'mail', 'plate']
    lst_of_accessories = ['back', 'neck', 'ring']
    lst_of_weapon_slots = ['one hand', 'two hand', 'off-hand']
    lst_of_tier = ['tier']
    if str(armor_type).lower() in lst_of_tier:
        return True
    if str(armor_type).lower() in lst_of_accessories:
        return True
    if str(armor_type).lower() in lst_of_armor_tiers:
        if str(armor_type).lower() == str(instance.armor):
            return True
        else:
            return False
    if str(slot).lower() in lst_of_weapon_slots:
        for weapon_og in instance.weapons:
            weapon = str(weapon_og).lower()
            weapon = weapon.lower().replace('off-hand', 'oh - int')
            weapon = weapon.lower().replace('axe 1h', '1h axe')
            weapon = weapon.lower().replace('mace 1h', '1h mace')
            weapon = weapon.lower().replace('sword 1h', '1h sword')
            weapon = weapon.lower().replace('axe 2h', '2h axe')
            weapon = weapon.lower().replace('mace 2h', '2h mace')
            weapon = weapon.lower().replace('sword 2h', '2h sword')
            if weapon in str(armor_type).lower():
                if ' - ' in str(armor_type).lower():
                    if str(instance.primary_stat) in str(armor_type).lower():
                        return True
                else:
                    return True

    if str(slot).lower() == 'trinket':
        trinket_type = str(armor_type).lower()
        trinket_mainstat = str(mainstat).lower()
        role = str(instance.role)
        primary_stat = str(instance.primary_stat)
        if trinket_type == 'all':
            return True
        elif trinket_type == 'tank' and role == 'tank':
            return True
        elif trinket_type == 'healer' and role == 'healer':
            return True
        elif trinket_type == 'tank | healer' and role == 'tank':
            return True
        elif trinket_type == 'tank | healer' and role == 'healer':
            return True
        elif trinket_type == 'caster' and primary_stat == 'int':
            return True
        elif trinket_type == 'mdps' and (primary_stat in trinket_mainstat):
            return True
        elif trinket_type == 'rdps' and (primary_stat in trinket_mainstat):
            return True
        elif trinket_type == 'mdps' and primary_stat == 'str' and trinket_mainstat == 'mastery':
            return True
        elif trinket_type == 'mdps' and primary_stat == 'str' and trinket_mainstat == 'crit':
            return True
        elif trinket_type == 'mdps' and primary_stat == 'agi' and trinket_mainstat == 'crit':
            return True
        elif trinket_type == 'rdps' and primary_stat == 'agi' and trinket_mainstat == 'mastery':
            return True
        elif trinket_type == 'rdps' and primary_stat == 'int' and trinket_mainstat == 'mastery':
            return True
    return False

# Define the Filter() function
def filter_loot(df, instance, item_name):
    # get relevant df row
    row = df[df[name] == item_name]
    if not row.empty:
        armor_type = row.iloc[0][armor_tier]
        slot = row.iloc[0][itemtype]
        mainstat = row.iloc[0][catagory_mainstat]
    else:
        assert(False)
    if loot_type_compatibility(armor_type, slot, mainstat, instance):
        return True
    else:
        return False

def shorten_string(s):
    if len(s) > 4:
        # Check if there's a space at position 3 or 4
        space_pos = s.find(' ', 2, 4)
        if space_pos != -1:
            # If there is a space, shorten to the position before the space
            s = s[:space_pos]
        else:
            # Otherwise, just take the first 5 characters
            s = s[:4]
    return s

def get_stats(df, item_name):
    # Find the row in the DataFrame that contains an element matching str_A in the "Name" column
    row = df[df[name] == item_name]
    if not row.empty:
        # Return the value in the "Mainstat" column of that row
        mainstat = row.iloc[0][catagory_mainstat]
        #operator = row.iloc[0]['Operator']
        operator = '>'
        secondarystat = row.iloc[0]['Sec Stat']
        summary = f'{mainstat} {operator} {secondarystat}'
        if (row.iloc[0][itemtype] == 'Trinket'):
            trinketname = row.iloc[0][name]
            trinketname = shorten_string(trinketname)
            return trinketname
        elif (row.iloc[0][armor_tier] == 'Tier'):
            return 'Tier'
        return summary
    else:
        # If no row contains the specified element, return None
        return None

def rename_instances_in_df(df):
    dungeon_shortener = "M+: "
    raid_shortener = "Raid: "
    dungeons = ['Brackenhide Hollow', 'Halls of Infusion',
                'Neltharus', 'Uldaman', 'Freehold', "Neltharion's Lair",
                'Underrot', 'Vortex Pinnacle']
    raidbosses = ['Kazzara', 'Amalgamation', 'Experiments', 'Zaqali',
                  'Rashok', 'Zskarn', 'Magmorax', 'Neltharion', 'Sarkareth']
    #for dungeon in dungeons:
    #    sourced = dungeon_shortener + dungeon
    #    df[catagory].replace(dungeon, sourced, inplace=True)
    #for raid in raidbosses:
    #    sourced = raid_shortener + raid
    #    df[catagory].replace(raid, sourced, inplace=True)
    #my_var = "M+ Raid: Neltharion's Lair"
    #new_var = "M+ Neltharion's Lair"
    #df[catagory].replace(my_var, new_var, inplace=True)
    df[itemtype].replace('Shoulders', 'Shoulder', inplace=True)
    # Dungeon shortening

    for i, dungeon in enumerate(dungeons):
        df[catagory].replace(dungeon, shortened_dungeons[i], inplace=True)
    for i, raidboss in enumerate(raidbosses):
        df[catagory].replace(raidboss, shortened_raidboss[i], inplace=True)
    return df


def calculate_percentages(df_counts):
    column_sums = df_counts.sum()

    # add a new row containing the column sum to the dataframe
    df_counts = pd.concat([df_counts, pd.DataFrame(column_sums).T.rename(index={0: vault_sum})])

    # calculate the row sum
    row_sum = df_counts.iloc[:, 0:].sum(axis=1)
    # replace each element with its percentage
    df_counts.iloc[:, 0:] = df_counts.iloc[:, 0:].apply(lambda x: round(100 * x / row_sum[x.index], 0), axis=0)
    # format percentages to not go "11.0"
    df_counts = df_counts.applymap(lambda x: '{:.0%}'.format(x/100) if isinstance(x, (float, int)) else x)
    for small_percentage in ["0%"]:
        df_counts.replace(small_percentage, "-", inplace=True)
    return df_counts


def reorder_dataframe_columns(df, column_order_list):
    existing_columns = df.columns.tolist()
    reordered_columns = [col for col in column_order_list if col in existing_columns]
    reordered_columns += [col for col in existing_columns if col not in column_order_list]
    return df[reordered_columns]

def reorder_columns(df_input):
    # Define the desired order of columns
    desired_order = ['Head', 'Shoulder', 'Chest', 'Hands', 'Legs',
                     'Wrist', 'Waist', 'Feet',
                     'One Hand', 'Off-hand', 'Two Hand',
                     'Neck', 'Back', 'Ring', 'Trinket']
    # Reorder the columns
    df_reordered = reorder_dataframe_columns(df_input, desired_order)
    return df_reordered

def generate_counts_table(df, instance):
    df = rename_instances_in_df(df)
    # Apply the Filter() function to each name in the DataFrame, and only add the name to the list if Filter() returns True
    df_filtered = df[df[name].apply(lambda x: filter_loot(df, instance, x))].reset_index(drop=True)
    # Rename the name of the item to its stats
    df_filtered[name] = df_filtered[name].apply(lambda x: get_stats(df_filtered, x))
    # Count number of items
    df_counts = pd.crosstab(index=df_filtered[catagory], columns=df_filtered[itemtype])
    df_counts = calculate_percentages(df_counts)
    df_counts = reorder_columns(df_counts)
    # Reorder the rows
    df_counts = df_counts.reindex(shortened_dungeons+[vault_sum])
    return df_counts

def generate_pivot_table(df, instance):
    df = rename_instances_in_df(df)
    # Apply the Filter() function to each name in the DataFrame, and only add the name to the list if Filter() returns True
    df_filtered = df[df[name].apply(lambda x: filter_loot(df, instance, x))].reset_index(drop=True)
    # Rename the name of the item to its stats
    df_filtered[name] = df_filtered[name].apply(lambda x: get_stats(df_filtered, x))

    # Group the filtered DataFrame by category and type, and apply the tolist method to the groups to get lists of names
    df_names = df_filtered.groupby([catagory, itemtype])[name].apply(list).reset_index()
    # Pivot the DataFrame to put categories on one axis and types on another axis
    df_pivot = df_names.pivot(index=catagory, columns=itemtype, values=name)

    df_pivot = reorder_columns(df_pivot)
    # Reorder the rows
    if filename == "wow_items_s2_dungeons_only":
        df_pivot = df_pivot.reindex(shortened_dungeons)
    elif filename == "wow_items_s2_raid_only":
        df_pivot = df_pivot.reindex(shortened_raidboss)

    df_pivot = pivot_format(df_pivot)
    return df_pivot

def pivot_format(df_pivot):
    # define function to extract first element of a list if it has more than one element
    def extract_first_element(x):
        if isinstance(x, list) and len(x) == 1:
            my_str = x[0]
        elif isinstance(x, list) and len(x) == 2:
            my_str = x[0]+','+x[1]
        elif isinstance(x, list) and len(x) == 3:
            my_str = x[0]+','+x[1]+','+x[2]
        elif isinstance(x, list) and len(x) == 4:
            my_str = x[0]+','+x[1]+','+x[2]+','+x[3]
        elif isinstance(x, list) and len(x) > 4:
            my_str = '5+'
        else:
            return x
        my_str = my_str.replace(' ', '')
        my_str = my_str.replace(',', ', ')
        """
        my_str = my_str.replace('M>', '🟠>')
        my_str = my_str.replace('H>', '🟢>')
        my_str = my_str.replace('C>', '🟡>')
        my_str = my_str.replace('V>', '🔵>')
        my_str = my_str.replace('>M', '🟠')
        my_str = my_str.replace('>H', '🟢')
        my_str = my_str.replace('>C', '🟡')
        my_str = my_str.replace('>V', '🔵')
        """

        return my_str
    df_pivot = df_pivot.fillna('-')

    # apply function to all elements in the dataframe
    df_pivot = df_pivot.applymap(extract_first_element)

    return df_pivot

def iterate_over_specs(df):
    count_tables = {}
    pivot_tables = {}
    instances = initialize_spec_objects()
    counter = 1
    for instance in instances:
        print(f'({counter}/{len(instances)}): Processing {instance.specname}')
        spec_alias = instance.class_color+instance.specname
        counter += 1
        pivot_table = generate_pivot_table(df, instance)
        pivot_tables[spec_alias] = pivot_table
        count_table = generate_counts_table(df, instance)
        count_tables[spec_alias] = count_table
    return pivot_tables, count_tables


def remove_non_ascii_chars(s):
    return ''.join(['?' if ord(c) > 127 else c for c in s])

def save_as_txt_file(string):
    filename = "testfile.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(string)

def fix_table_add(element):
    if isinstance(element, str) and '%' in element:
        return element + ': '
    else:
        return element

# define a function to replace 'A' with 'B' in a string
def replace_A_with_B(s):
    return s.replace('%', '%: ')

def add_caret(df_for_reddit):
    #for col in df_for_reddit.columns:
    #    df_for_reddit[col] = '^' + df_for_reddit[col].astype(str)
    #return df_for_reddit
    #new_df = df_for_reddit.applymap(lambda x: ' '.join(['^' + w if w else '' for w in x.split()]))
    #return new_df

    # Add caret to column headers
    new_cols = []
    for col in df_for_reddit.columns:
        words = col.split()
        for i in range(len(words)):
            words[i] = '^' + words[i]
        new_cols.append(' '.join(words))
    df_for_reddit.columns = new_cols

    # Add caret to row indexes and values
    for i in range(len(df_for_reddit.index)):
        row_name = df_for_reddit.index[i]
        words = row_name.split()
        for j in range(len(words)):
            words[j] = '^' + words[j]
        new_row_name = ' '.join(words)
        df_for_reddit = df_for_reddit.rename(index={row_name: new_row_name})

        for j in range(len(df_for_reddit.columns)):
            col_name = df_for_reddit.columns[j]
            row_value = df_for_reddit.iloc[i, j]
            if isinstance(row_value, str):
                words = row_value.split()
                for k in range(len(words)):
                    words[k] = '^' + words[k]
                new_value = ' '.join(words)
                df_for_reddit.iat[i, j] = new_value
    return df_for_reddit

def pandas_to_reddit_table_single(specname, single_df):
    # Get column names and add separator row
    #single_df = add_caret(single_df)
    separator = ' | '.join(['---'] * (len(single_df.columns)+1))
    header = ' | '.join([''] + list(single_df.columns) + [''])
    table = [header, separator]
    # Add rows to table
    for i, row in single_df.iterrows():
        row_str = ' | '.join([str(i)] + [str(val) for val in row.values] + [''])
        table.append(row_str)

    reddit_table = '\n'.join(table)
    if filename == "wow_items_s2_dungeons_only":
        stamp = 'M+ s2'
    elif filename == "wow_items_s2_raid_only":
        stamp = 'Raid s2'
    named_reddit_table = stamp + reddit_table
    return named_reddit_table

"""
def pandas_to_reddit_table_double(specname, df_percents, df_stats):
    # Get column names and add separator row
    #df_percents = add_caret(df_percents)
    #df_stats = add_caret(df_stats)
    separator = ' | '.join(['---'] * (len(df_percents.columns)+1))
    header = ' | '.join([''] + list(df_percents.columns) + [''])
    table = [header, separator]
    table_percents = []
    table_stats = []

    # Add rows to table
    for i, row in df_percents.iterrows():
        row_str = ' | '.join([str(i)] + [str(val) for val in row.values] + [''])
        table_percents.append(row_str)

    for i, row in df_stats.iterrows():
        row_str = ' | '.join([str(i)] + [str(val) for val in row.values] + [''])
        for dungeon in shortened_dungeons:
            row_str = row_str.replace(dungeon, "Item stats:")
        row_end = '|'.join([str(i)] + [str("") for val in row.values] + [''])
        for dungeon in shortened_dungeons:
            row_end = row_end.replace(dungeon, "")
        row_full = row_str + '\n' + row_end
        table_stats.append(row_full)

    # Join rows and return table string
    merged_rows = [elem for pair in zip(table_percents, table_stats) for elem in pair]
    table = table + merged_rows
    reddit_table = '\n'.join(table)
    outside_table = f'***\n  \n&nbsp;  \n  \n#{specname}  \n  \n'
    named_reddit_table = outside_table + 'M+ s2' + reddit_table
    return named_reddit_table
"""

def outside_table(specname):
    #return f'\n  \n***\n  \n&nbsp;  \n  \n#{specname}  \n  \n'
    return f'\n***\n&nbsp;\n#{specname}  \n  \n'

def find_tables(input_str):
    table_starts = []
    table_ends = []
    for i in range(len(input_str)):
        if input_str[i:i+10] == 'tableStart':
            table_starts.append(i)
        elif input_str[i:i+8] == 'tableEnd':
            table_ends.append(i)

    table_contents = []
    for start, end in zip(table_starts, table_ends):
        table_contents.append(input_str[start+11:end])

    return table_contents

def main_function(df, mode, lst_of_tables):
    table_strings = {}
    duplicates = 0
    pivot_tables, count_tables = iterate_over_specs(df)
    previous_table_string = ""
    previous_spec_name = ""
    for count, specname in enumerate(pivot_tables):
    #for specname in pivot_tables:
        pivot_table = pivot_tables[specname]
        pivot_table = pivot_table.transpose()
        count_table = count_tables[specname]
        count_table = count_table.transpose()

        if filename == "wow_items_s2_dungeons_only":
            last_col = count_table.iloc[:, -1]
            pivot_table = pd.concat([pivot_table, last_col], axis=1)
        #new_table = count_table.add(pivot_table)
        #new_table = new_table.applymap(replace_A_with_B)
        #new_table.replace("--", "-", inplace=True)
        #table_string = pandas_to_reddit_table(specname, new_table
        if mode == "count":
            table_string = pandas_to_reddit_table_single(specname, count_table)
        elif mode == "pivot":
            table_string = pandas_to_reddit_table_single(specname, pivot_table)
        else:
            table_string = ""
        #table_string = table_string.replace("^^", "^")
        table_string = table_string.replace("| ", "|")
        table_string = table_string.replace(" |", "|")
        table_string = table_string.replace("Hands", "Hand")
        #table_string = table_string.replace("Trinket", "Trin-ket")
        #table_string = table_string.replace("Shoulder", "Sho-ulder")
        table_string = table_string.replace("Amalgamation", "Amalga")
        table_string = table_string.replace("Experiments", "Experim.")
        if previous_table_string == table_string:
            new_spec_title = previous_spec_name + ' + ' + specname
            table_strings.pop(previous_spec_name)
            duplicates += 1
        else:
            new_spec_title = specname
        if len(lst_of_tables) == 0:
            table_strings[new_spec_title] = outside_table(new_spec_title)+'tableStart\n'+table_string+'\ntableEnd'
            previous_spec_name = new_spec_title
            previous_table_string = table_string
        else:
            matching_table = lst_of_tables[count-duplicates]
            separator = '\n  \n***\n  \n&nbsp;  \n  \n'
            separator = '\n  \n&nbsp;  \n  \n'
            table_strings[new_spec_title] = outside_table(new_spec_title)+table_string+separator+matching_table
            previous_spec_name = new_spec_title
            previous_table_string = table_string

    long_string = ""
    for table in table_strings:
        long_string = long_string + table_strings[table]
        if len(lst_of_tables) != 0:
            print(table_strings[table])
    if len(lst_of_tables) != 0:
        save_as_txt_file(long_string)
    return find_tables(long_string)




#%%
if __name__ == "__main__":
    #mode = "count"
    mode = "pivot"
    filename = "wow_items_s2_raid_only"
    df = pd.read_csv(f'{filename}.csv', sep=';')
    dungeon_table_lst = main_function(df, mode, [])

    mode = "pivot"
    filename = "wow_items_s2_dungeons_only"
    df = pd.read_csv(f'{filename}.csv', sep=';')
    raid_table_lst = main_function(df, mode, dungeon_table_lst)
