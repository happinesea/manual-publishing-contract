# Version Contract v0.1

> This document is a translation. The Japanese specification is canonical in case of discrepancies.

`family_id` identifies a manual family, `manual_id` identifies one language/version edition, and `version` records that edition. Product identity and manual identity MUST NOT be treated as identical.

`supersedes` MAY refer to the replaced manual ID, but it is not a deletion instruction. Multiple versions may remain published, deprecated, or archived at the same time.
