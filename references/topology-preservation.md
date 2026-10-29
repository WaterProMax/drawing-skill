# Topology Preservation Policy

Technical diagrams encode meaning through connectivity and containment.

## Topology includes

- nodes;
- arrows and arrowheads;
- connector endpoints;
- line direction;
- solid/dashed semantics;
- loops;
- branches;
- shared rails/buses;
- group/container boundaries;
- parent-child containment;
- layer/order relationships.

## Edit default

```yaml
preserve_topology: true
```

Unless the user explicitly requests a structural change, topology is immutable.

## Required verification

After every edit, compare:

- node count and IDs;
- relation count and IDs;
- source/target endpoints;
- arrowhead locations;
- branch conditions;
- containment membership;
- loop closure;
- boundary completeness.

A broken border, clipped connector, missing arrowhead, or rerouted endpoint is a semantic regression.

## Local edit rule

A text/icon/color edit may not modify connector geometry or group boundaries unless explicitly authorized.

## High-risk escalation

If topology is dense or exact endpoint preservation cannot be verified visually, use a deterministic renderer or vector/object source.

## Relation ledger

Formerly `relation-ledger.md`. Record every semantic relation before generation or editing, then check the visible figure against the ledger.

```yaml
relations:
  - id: r01
    source: ""
    target: ""
    relation: ""
    direction: forward
    line_style: solid
    label: null
    required: true
```

After generation record visible source, target, arrowhead endpoint, line style, and traceability. Reject ambiguous shared rails.

The editable template is `templates/relation-ledger.yaml`. A text, icon, or color edit may not rewrite this ledger unless the Edit Contract lists those relations as mutable.
