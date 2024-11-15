# Config Management

## Config as Code with Nitpick

In general, we aim to manage configurations "as code" wherever reasonable to maintain a baseline of declarative settings.

Nitpick is a tool used for managing configuration files across multiple projects. It helps enforce consistency and best practices by allowing you to define and enforce configuration standards.

### Enforcing Standards with Nitpick

In this repository, we use Nitpick to enforce configuration standards through the following files:

1. **Core Standards (`nitpick/core.toml`)**: Essential configurations consistent across all projects, ensuring baseline quality and structure.

2. **Stylistic Preferences (`nitpick/style.toml`)**: Opinionated settings for code style and formatting, flexible and subject to team preferences.

3. **Project-Specific Configurations (`nitpick/strangebasis.toml`)**: Configurations tailored to the specific needs of this project.

This same design pattern is scaffolded for you in the "cookiecut" projects. [Considerations for maintaining these paradigms are also documented in the "cut" projects](../{{cookiecutter.project_name}}/docs/config.md) already.

### Benefits of This Approach

- **Consistency**: By separating core standards from project-specific and stylistic configurations, you ensure that essential settings are consistently applied across all projects.
- **Flexibility**: This approach allows you to easily update and change stylistic preferences without affecting the core standards.
- **Modularity**: You can easily add or remove configuration files based on the needs of your project. For example, if you start a new project in a different language, you can create a new configuration file specific to that language.

### Comprehensive and Flexible Design

To be more comprehensive but flexible for design changes later on, consider the following:

- **Modular Configuration Files**: Break down your configurations into smaller, modular files that can be easily combined and extended.
- **Version Control**: Use version control to manage changes to your configuration files. This allows you to track changes and revert to previous versions if needed.
- **Documentation**: Document your configuration files and the rationale behind each setting. This helps team members understand the purpose of each configuration and makes it easier to update them in the future.
  - document strict/enforced settings in the nitpick toml file
  - document user preferences/runtime settings in the config files themselves
  - document high level config information in this document!

By following this approach, you can create a robust and flexible configuration management system that adapts to the evolving needs of your projects.

### References and Additional Resources

- [Nitpick Documentation](https://nitpick.readthedocs.io/en/latest/)
- [Config as Code: Best Practices](https://www.redhat.com/en/topics/automation/what-is-configuration-as-code)
- [Managing Configuration Files with Nitpick](https://realpython.com/python-nitpick/)
- [Version Control for Configuration Files](https://www.atlassian.com/git/tutorials/saving-changes)
- [Modular Configuration Management](https://martinfowler.com/articles/microservice-testing/#modular-config)
