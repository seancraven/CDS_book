## The Relational Alternative
The previous pages' example has its data rearranged and transformed into a relational database  
```{mermaid}
:align: center
:caption: A relational database alternative to transaction data storage, which provides reduced data duplication.
erDiagram
    customer o|--|{transaction_: ""
    customer{
    customer_id int PK
    card_number int 
    loyalty_card bool 
    }
    transaction_ }o--|| item : ""
    transaction_{
    transaction_id int PK
    coustomer_id int FK
    item_id int FK
    }
    item{
    item_id int PK
    price float
    item_name string 
}
```

In the schema above, the values in the table boxes indicates the column name and type for each entry. The PK symbol in the last column of the tables indicates if that column corresponds to a primary key.

A primary key is a unique entry or unique combination of entries, which identify a row in a table. This is often an integer or a fixed length string. This key can then be used to relate one table to another as a foreign key. 

The foreign key is the primary key of one table stored in a row of another table. If we had a customer; Obi-wan who has coustomer_id 0, this will be the same in both the customer table and the transaction table and can be used to query both tables. 

When the database is queried and asked for fields in two or more tables, for instance a query for transactions price, item_name, and card number, for a given transaction id. The item_id and customer_id from the transaction can be used to "join" the tables rows and return all the relevant values, while not storing that data duplicated in one table. A caveat being, space reduction assumes that an item is sold more than once and some customers buy more than one thing.

The links between the tables are denoted by [crow's foot notation](https://en.wikipedia.org/wiki/Entity%E1%80%93relationship_model#Crow's_foot_notation):
![crow's_foot](../Figures/crows_foot.png)

This leaves the question how does one build a database? Conveniently, python itself comes with a SQLite database implementation, and one can build databases, store data and retrieve data, without ever leaving a python script. 

There are examples of sql queries to construct, fetch and insert data in the calculate_optical_depths_from_hitran.py file found in the SimpleTrans package. Additionally, the SQLite3 documentation has [examples](https://www.sqlitetutorial.net/sqlite-python/).
