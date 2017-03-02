---
title: MySQL常用知识
author: Xiao Wenbin
date: 2016/09/26
category: mysql
---

## Table Join

用于连接的两个表如下所示：

`customer`表

| id   | username |
| ---- | -------- |
| 1    | tom      |
| 2    | john     |
| 3    | lucy     |

`order`表

| id   | customer_id | name   |
| ---- | ----------- | ------ |
| 1    | 2           | apple  |
| 2    | 4           | orange |
| 3    | 1           | pear   |

### Cross Join

Cross join表示两个数据表的笛卡尔积。

SQL命令如下：

```mysql
SELECT * FROM `customer`, `order`;
SELECT * FROM `customer` cross join `order`;
```

结果如下：

| customer.id | username | order.id | customer_i | name   |
| ----------- | -------- | -------- | ---------- | ------ |
| 1           | tom      | 1        | 2          | apple  |
| 1           | tom      | 2        | 4          | orange |
| 1           | tom      | 3        | 1          | pear   |
| 2           | john     | 1        | 2          | apple  |
| 2           | john     | 2        | 4          | orange |
| 2           | john     | 3        | 1          | pear   |
| 3           | lucy     | 1        | 2          | apple  |
| 3           | lucy     | 2        | 4          | orange |
| 3           | lucy     | 3        | 1          | pear   |

### Inner Join

Inner Join表示两个数据表中匹配数据行

```mysql
SELECT * FROM `customer`, `order` WHERE `customer`.`id` = `order`.`customer_id`;
SELECT * FROM `customer` INNER JOIN `order` ON `customer`.`id` = `order`.`customer_id`;
```

返回结果：

| customer.id | username | order.id | customer_id | name  |
| ----------- | -------- | -------- | ----------- | ----- |
| 1           | tom      | 3        | 1           | pear  |
| 2           | john     | 1        | 2           | apple |

### Left/Right Join

两个数据表的匹配数据行以及left表或right表中不匹配的数据行

```mysql
SELECT * FROM `customer` LEFT JOIN `order` ON `customer`.`id` = `order`.`customer_id`
```

left join返回结果：

| customer.id | username | order.id | customer_id | name  |
| ----------- | -------- | -------- | ----------- | ----- |
| 1           | tom      | 3        | 1           | pear  |
| 2           | john     | 1        | 2           | apple |
| 3           | lucy     | null     | null        | null  |

right join返回结果：

| customer.id | username | order.id | customer_id | name   |
| ----------- | -------- | -------- | ----------- | ------ |
| 1           | tom      | 3        | 1           | pear   |
| 2           | john     | 1        | 2           | apple  |
| null        | null     | 2        | 4           | orange |

### Self Join

表`address`

| id   | parent_id | name |
| ---- | --------- | ---- |
| 1    | 0         | 中国   |
| 2    | 1         | 浙江   |
| 3    | 2         | 杭州   |

表跟自己连接

```mysql
SELECT a.name as parent, b.name as child FROM address as a, address as b where a.id = b.parent_id;
```

返回结果：

| parent | child |
| ------ | ----- |
| 中国     | 浙江    |
| 浙江     | 杭州    |