### Create Focused Agent Tasks

Each agent gets:
- **Specific scope:** One independent responsibility and the callers affected by its contract
- **Clear goal:** Complete the required behavior through its real entrypoints
- **Constraints:** Respect the authorized scope and other work; coordinate changes to shared owners
- **Expected output:** The implemented result, any changed consumer contract, and remaining blockers

## Agent Prompt Structure

Good agent prompts are:
1. **Focused** - One clear problem domain
2. **Self-contained** - All context needed to understand the problem
3. **Specific about output** - What should the agent return?

## When NOT to Use

**Related failures:** Fixing one might fix others - investigate together first
**Need full context:** Understanding requires seeing entire system
**Exploratory debugging:** You don't know what's broken yet
**Shared state:** Agents would interfere (editing same files, using same resources)
