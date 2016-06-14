create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Sentences about siblings that are the same size
create table sentences as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
create table above_average as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

-- Question 1: Composites --
create table composites as
   select distinct a.n * b.n as c from ints as a, ints as b where a.n* b.n <= 100 and a.n <>1 and b.n <> 1;

create table multiples as
   select c as m from composites union all select n from ints;

-- Question 2: Primes --
create table primes as
   select m as p from multiples group by m having count(m) < 2 and m <> 1;
