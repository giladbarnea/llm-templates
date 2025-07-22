Capture the **Architectural Intent** or the **Guiding Philosophy** of the code.

**Architecture & Extension Guide**

This document explains the core design philosophy of `<file/module/project etc>` to help you add new features easily and maintainably.

**1. The Guiding Philosophy**

The central idea is that: [central idea]
We don't have [negative example]. Instead, we have [positive example].

The main reason for this design is to make the script easy to extend. Adding a new feature should feel like adding a new, self-contained module, not like performing surgery on the core logic.

**2. The Lifecycle of a Change**

Any change you propose will follow this journey:

[Numbered list of flow stages from start to finish]

**3. How to Add a New Feature**

Let's say you want to add a feature to [toy feature example]. Here’s how you’d do it by following the pattern:

[Numbered list of... what exactly?]

That's it. Notice you didn't have to [examples of actions that would make the code rotten and everyone else frustrated]. You just [description of the minimal, elegant actions that were performed thanks to the architecture].


---

(verbose version)

# Architecture & Extension Guide

**Purpose:** This document explains the core design philosophy of `[Project/Module Name]` to help you add new features easily and in a way that aligns with the existing architecture. Its goal is to make your life easier and the codebase healthier.

## 1. The Guiding Philosophy (The "Why")

The central idea is that **`[describe the core abstraction in one clear sentence. e.g., "every business operation is a self-contained Command object," or "every UI section is a Component that manages its own state"]`**.

To achieve this, we avoid patterns like `[describe the anti-pattern, e.g., "a single master function with a large switch/case statement that handles all operations"]`. Instead, we prefer a structure where `[describe the positive pattern, e.g., "we have many small Command classes, and the system knows how to run any of them without knowing what they do internally"]`.

The primary reason for this design is to **reduce complexity and coupling**. When you add a new feature, it should feel like adding a new, independent module, not performing delicate surgery on a central, critical piece of code.

## 2. The Lifecycle of a [Core Abstraction Name] (The "How")

Any new piece of functionality generally follows this data flow or lifecycle. Understanding this path is key to knowing where your code should go.

1.  **Creation/Instantiation:**
    `[Describe where and how your core abstraction is born. e.g., "A `Command` object is created by a `Factory` based on an incoming API request."]`

2.  **Configuration/Processing:**
    `[Describe what happens to the object after it's created. e.g., "The `Command` is passed to a `Pipeline` that attaches necessary context, like the current user and a database connection."]`

3.  **Execution:**
    `[Describe the main action. e.g., "The application calls the `execute()` method on the `Command` object. The `Command` itself contains all the logic to perform its specific task."]`

4.  **Consumption/Termination:**
    `[Describe what happens to the result. e.g., "The result from `execute()` is then passed to a `Serializer` to be formatted as a JSON response."]`

## 3. How to Add a New Feature (The "What")

Let's walk through a tangible example. Say you want to add a feature to `[describe a simple, analogous new feature, e.g., "add a new 'ExportUserData' operation"]`.

Here’s how you’d do it by following the established pattern:

1.  **Implement the Core Interface:**
    `[Describe the first concrete step—usually creating a new file or class that inherits from a base class or implements an interface. e.g., "Create a new class, `ExportUserDataCommand`, that inherits from our `BaseCommand`."]`

2.  **Encapsulate the Feature Logic:**
    `[Describe where the unique business logic for the new feature goes. e.g., "Inside your new class, implement the `execute()` method. This is where you'll query the database for the user's data and format it as a CSV."]`

3.  **Register the New Component:**
    `[Describe how the system is made aware of the new component. e.g., "In `api_routes.py`, add a new route that maps the `/export` endpoint to your `ExportUserDataCommand`."]`

That's it.

Notice you didn't have to `[list actions that would violate the architecture, e.g., "modify the central API request handler," "add an 'if/elif' statement to the core application loop," or "manually handle database connections"]`.

You just **`[summarize the simple, elegant actions the architecture enabled, e.g., "created a new, self-contained class that holds the specific logic for this feature and then told the system how to trigger it"]`**.