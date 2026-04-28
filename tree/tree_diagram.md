# Visual Logic: The Daily Reflection Tree

This diagram illustrates the deterministic branching logic across the three axes: Locus, Orientation, and Radius.

```mermaid
graph TD
    %% Axis 1: Locus of Control
    START[Start Session] --> A1_OPEN[Day Description]
    A1_OPEN -- Productive/Mixed --> A1_D1{Decision 1}
    A1_OPEN -- Tough/Frustrating --> A1_D1
    
    A1_D1 -- High Agency Path --> A1_Q_AG_H[A1: Why Success?]
    A1_D1 -- Low Agency Path --> A1_Q_AG_L[A1: Initial Instinct?]
    
    A1_Q_AG_H -- Internal --> A1_R_INT[Reflection: Agency Identified]
    A1_Q_AG_H -- External --> A1_R_EXT[Reflection: External Focus]
    
    A1_Q_AG_L -- Internal --> A1_R_INT
    A1_Q_AG_L -- External --> A1_R_EXT

    %% Axis 2: Orientation
    A1_R_INT --> BRIDGE1[Bridge to Axis 2]
    A1_R_EXT --> BRIDGE1
    BRIDGE1 --> A2_OPEN[A2: Key Interaction]
    
    A2_OPEN -- Helping/Extra --> A2_R_CONT[Reflection: Contribution]
    A2_OPEN -- Overlooked/Ignored --> A2_R_ENT[Reflection: Entitlement]

    %% Axis 3: Radius
    A2_R_CONT --> BRIDGE2[Bridge to Axis 3]
    A2_R_ENT --> BRIDGE2
    BRIDGE2 --> A3_OPEN[A3: Who was Affected?]
    
    A3_OPEN -- Team/User --> A3_R_ALTRO[Reflection: Altrocentrism]
    A3_OPEN -- Just Me --> A3_R_SELF[Reflection: Self-Centrism]

    %% Closing
    A3_R_ALTRO --> SUMMARY[Final Summary]
    A3_R_SELF --> SUMMARY
    SUMMARY --> END[End Session]
