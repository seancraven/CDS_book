(rd)=
### A very short introduction to relational databases
Relational databases have become ubiquitous in modern-day life, with logins and Airbnb being common uses. For this book, we build our database and interact with the HITRAN database. 

A relational database is a structured approach to storing data. It describes a group of tables that are related together. The relationships enable a reduction of data duplication. Typically, these databases are interfaced and queried with using [SQL](https://en.wikipedia.org/wiki/SQL). One of the few programming languages used for about 50 years.
```{margin}
Modern Datatbase applications are oftend distributed over a wide variety of nodes, individual computers, this has a much more complex backend to store partial databases. However, many of these formats have a SQL like interface that can be used to abstract away much of the complexity. [Apache Spark](https://spark.apache.org/sql/) is a great example of this.
``` 
```{note}
If you are interested in learning SQL, [this textbook](https://www.google.co.uk/books/edition/Learning_SQL/YqubAgAAQBAJ?hl=en&gbpv=0) is great.
```
Relational databases reduce duplication by separating out repeated values. For example, If one was to store some data on a customer in a shop, one might store a table as follows,
```{mermaid}
:align: center
:caption: A table of important information associated with some transaction for a shop.
erDiagram
    transaction{
    transaction_id int
    coustomer_id int
    item_id int 
    item_name string
    price float
    card_number int
    loyalty_card bool
    }
```

It should be evident that storing all of these fields for each transaction would be wasteful if a customer regularly bought more than one item. When using a relational database, the number of repeat entries can be cut down by creating multiple tables and linking one table that contains information about a customer to another table that contains information about transactions. This can be described in an entity relationship diagram depicted on the next page.
```{note}
These two pages are split to avoid a bug with Jupyter-Book.
``` 