HBNB Evolution Group project #2

High Level Package Diagram:

'''mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +ServiceAPI
    +UserService
    +PlaceService
    +ReviewService
    +AmenityService
}
class BusinessLogicLayer {
    +ModelClasses
    + Users
    + Place
    + Review
    + Amenities
}
class PersistenceLayer {
    +DatabaseAccess
    + UserRepository
    +PlaceRepository
    +ReviewRepository
    +AmenityRepository
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
'''


Class Diagram Business Logic Layer:

'''mermaid
classDiagram
class User {
    +UUID4 id
    +String FirstName
    +String lastname
    +String email
    +String password
    +boolean Admin
    +Date createdAt
    +Date updatedAt
    +register()
    +updateProfile()
    +delete()
}
class Place {
    +UUID4 id
    +String title
    +String description
    +float price
    +float latitude
    +float longitude
    +List~Amenity~ amenities
    +Date createdAt
    +Date updatedAt
    +create()
    +update()
    +delete()
    +list()
}
class Review {
    +UUID4 id
    +int rating
    +String comment
    +Date createdAt
    +Date updatedAt
    +create()
    +update()
    +delete()
    +listByPlace()
}
class Amenity {
    +UUID4 id
    +String name
    +String description
    +Date createdAt
    +Date updatedAt
    +create()
    +update()
    +delete()
    +list()
}
User "1" --> "0..*" Place : owns
Place "1" --> "0..*" Review : has
Place "0..*" --> "0..*" Amenity : includes
'''


Sequence Diagram User Registration:

'''mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Register User
API->>BusinessLogic: Validate and Process Registration
BusinessLogic->>Database: Save User Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Registration Success/Failure
API-->>User: Return Success/Failure
'''


Sequence Diagram Place Creation:

'''mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Create Place
API->>BusinessLogic: Validate and Process Place Creation
BusinessLogic->>Database: Save Place Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Place Creation Success/Failure
API-->>User: Return Success/Failure
'''


Sequence Diagram Review Submission:

'''mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Submit Review
API->>BusinessLogic: Validate and Process Review Submission
BusinessLogic->>Database: Save Review Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Review Submission Success/Failure
API-->>User: Return Success/Failure
'''


Fecthing a List of Places:

'''mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Fecthing a List of Places
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Retrieve Places Data
Database-->>BusinessLogic: Return Places Data
BusinessLogic-->>API: Return List of Places
API-->>User: Return List of Places
'''

