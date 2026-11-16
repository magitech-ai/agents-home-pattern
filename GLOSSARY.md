# Agent Home Pattern

Terms for discussing the emerging organization pattern. These definitions are
working vocabulary, not normative protocol language.

## Language

**Agent home repository**:
A version-controlled repository that groups shared agent guidance or resources
and provides orientation or navigation to related repositories.
_Avoid_: Universal agent configuration directory.

**Canonical source**:
The copy a team or individual intends to edit and maintain as authoritative.
It may be distinct from the locations a harness scans at runtime.
_Avoid_: Installed copy, discovery path.

**Discovery location**:
A filesystem path or other source that a particular agent harness scans for
guidance or skills.
_Avoid_: Standard location, unless a specific standard defines it.

**Discovery adapter**:
A link, copy, generated file, or other mechanism that makes canonical content
available through a harness's discovery location.
_Avoid_: Sync, when the mechanism does not actually synchronize changes.

**Pilot observation**:
A behavior directly exercised in a named setup, or explicitly attributed to
that setup. It does not imply the same behavior in other environments.
_Avoid_: Ecosystem support.

**Protocol**:
A stable, documented agreement precise enough for independent implementations
to interoperate and be tested for conformance. This repository does not yet
define one.
_Avoid_: Pattern, when referring to a normative specification.
