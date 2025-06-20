Simplified version of the Refactoring exercise from Axel W. Berle's Scrum Alliance CSD training course.

### What is this repository for? ###

* Refactoring for basic Clean Coding and SOLID principles

### What should you do here?

* Check out how the following techniques have been applied:

> `Scenario Template`

### Branches

* 1-price-calculator-manual-test: no documentation is found, only a "manual" automated test.
* 2-price-calculator-with-unit-test: code is covered by unit tests.
* 3-price-calculator-renamed: methods and variables renamed
* 3b-price-calculator-SRP: main class broken down into smaller more cohesive classes
* 4-price-calculator-OCP: extension by inheritance
* 5a-price-calculator-LSP: introduction of a new training course type: OD-SF
* 5b-price-calculator-LSP: a solution, breaking the Liskov Substitution Principle

* 10a-price-calculator-BDD: setup for first scenario
* 10b-price-calculator-BDD-implementation: implementation

### Business Rules

#### The training courses and prices

* There are 3 types of training courses: CSD, CSM and CSPO
* The price of a training course is defined by the training company.
* Guaranteed minimum price of R$ 900,00 for a CSD, R$ 1000,00 for a CSM and R$ 1200,00 for a CSPO training.

#### Discounts

* The prices for the training courses listed on the website must be updated on a daily basis.
* Discounts are based on how early a training course seat is bought

* **Early Bird**: when buying a seat within 10 days prior the training course, there is a daily discount of R$ 30,00 for a
  CSD training, and R$ 20,00 for the other training courses.
* **Super Early Bird**: when buying a seat earlier than 10 days, then there is a fixed discount of R$ 500,00 for a CSM,
  and R$ 400,00 for the other training courses
* No discount applicable the day before the training course
* No discount applicable 5 days prior to the training course whenever there are less than 3 seats left
 
### Who do I talk to? ###

* Axel Wilhelm Berle
* axelberle@gmail.com
