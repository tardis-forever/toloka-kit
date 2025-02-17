from enum import Enum
from toloka.client.primitives.base import BaseTolokaObject
from toloka.client.primitives.operators import (
    ComparableConditionMixin,
    CompareOperator,
    IdentityConditionMixin,
    IdentityOperator
)
from typing import (
    Any,
    Dict,
    Optional
)

class RuleConditionKey(Enum):
    """An enumeration.
    """

    ACCEPTED_ASSIGNMENTS_COUNT = 'accepted_assignments_count'
    ACCEPTED_ASSIGNMENTS_RATE = 'accepted_assignments_rate'
    ASSESSMENT_EVENT = 'assessment_event'
    ASSIGNMENTS_ACCEPTED_COUNT = 'assignments_accepted_count'
    CORRECT_ANSWERS_RATE = 'correct_answers_rate'
    FAIL_RATE = 'fail_rate'
    FAST_SUBMITTED_COUNT = 'fast_submitted_count'
    GOLDEN_SET_ANSWERS_COUNT = 'golden_set_answers_count'
    GOLDEN_SET_CORRECT_ANSWERS_RATE = 'golden_set_correct_answers_rate'
    GOLDEN_SET_INCORRECT_ANSWERS_RATE = 'golden_set_incorrect_answers_rate'
    INCOME_SUM_FOR_LAST_24_HOURS = 'income_sum_for_last_24_hours'
    INCORRECT_ANSWERS_RATE = 'incorrect_answers_rate'
    NEXT_ASSIGNMENT_AVAILABLE = 'next_assignment_available'
    PENDING_ASSIGNMENTS_COUNT = 'pending_assignments_count'
    POOL_ACCESS_REVOKED_REASON = 'pool_access_revoked_reason'
    REJECTED_ASSIGNMENTS_COUNT = 'rejected_assignments_count'
    REJECTED_ASSIGNMENTS_RATE = 'rejected_assignments_rate'
    SKILL_ID = 'skill_id'
    SKIPPED_IN_ROW_COUNT = 'skipped_in_row_count'
    STORED_RESULTS_COUNT = 'stored_results_count'
    SUBMITTED_ASSIGNMENTS_COUNT = 'submitted_assignments_count'
    SUCCESS_RATE = 'success_rate'
    TOTAL_ANSWERS_COUNT = 'total_answers_count'
    TOTAL_ASSIGNMENTS_COUNT = 'total_assignments_count'
    TOTAL_SUBMITTED_COUNT = 'total_submitted_count'


class RuleCondition(BaseTolokaObject):
    def __init__(
        self,
        *,
        operator: Optional[Any] = None,
        value: Optional[Any] = None
    ) -> None:
        """Method generated by attrs for class RuleCondition.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    operator: Optional[Any]
    value: Optional[Any]


class ComparableRuleCondition(RuleCondition, ComparableConditionMixin):
    def __init__(
        self,
        operator: CompareOperator,
        *,
        value: Optional[Any] = None
    ) -> None:
        """Method generated by attrs for class ComparableRuleCondition.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[Any]


class IdentityRuleCondition(RuleCondition, IdentityConditionMixin):
    def __init__(
        self,
        operator: IdentityOperator,
        *,
        value: Optional[Any] = None
    ) -> None:
        """Method generated by attrs for class IdentityRuleCondition.
        """
        ...

    operator: IdentityOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[Any]


class AcceptedAssignmentsCount(ComparableRuleCondition):
    """How many times this assignment was accepted

    Don't be confused!!!
    This condition used only with 'AssignmentsAssessment' controller.
    And exist very similar condition 'AssignmentsAcceptedCount', that used only with 'AnswerCount' controller.
    Sorry about that.
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class AcceptedAssignmentsCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class AcceptedAssignmentsRate(ComparableRuleCondition):
    """Percentage of how many assignments were accepted from this performer out of all checked assignment
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class AcceptedAssignmentsRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class AssessmentEvent(IdentityRuleCondition):
    """Assessment of the assignment changes its status to the specified one

    This condition can work only with compare operator '=='.

    Attributes:
        value: Possible values:
            * conditions.AssessmentEvent.ACCEPT
            * conditions.AssessmentEvent.ACCEPT_AFTER_REJECT
            * conditions.AssessmentEvent.REJECT

    Example:
        How to increase task overlap when you reject assignment in delayed mode.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentsAssessment(),
        >>>     conditions=[toloka.conditions.AssessmentEvent == toloka.conditions.AssessmentEvent.REJECT],
        >>>     action=toloka.actions.ChangeOverlap(delta=1, open_pool=True),
        >>> )
        ...
    """

    class Type(Enum):
        """An enumeration.
        """

        ACCEPT = 'ACCEPT'
        ACCEPT_AFTER_REJECT = 'ACCEPT_AFTER_REJECT'
        REJECT = 'REJECT'

    def __init__(
        self,
        operator: IdentityOperator,
        value: Optional[Type] = None
    ) -> None:
        """Method generated by attrs for class AssessmentEvent.
        """
        ...

    operator: IdentityOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[Type]


class AssignmentsAcceptedCount(ComparableRuleCondition):
    """How many assignment was accepted from performer

    Don't be confused!!!
    This condition used only with 'AnswerCount' controller.
    And exist very similar condition 'AcceptedAssignmentsCount', that used only with 'AssignmentsAssessment' controller.
    Sorry about that.
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class AssignmentsAcceptedCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class CorrectAnswersRate(ComparableRuleCondition):
    """The percentage of correct responses

    Be careful, it may have different meanings in different collectors.
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class CorrectAnswersRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class FailRate(ComparableRuleCondition):
    """Percentage of wrong answers of the performer to the captcha
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class FailRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class FastSubmittedCount(ComparableRuleCondition):
    """The number of assignments a specific performer completed too fast
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class FastSubmittedCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class GoldenSetAnswersCount(ComparableRuleCondition):
    """The number of completed control tasks
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class GoldenSetAnswersCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class GoldenSetCorrectAnswersRate(ComparableRuleCondition):
    """The percentage of correct responses in control tasks
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class GoldenSetCorrectAnswersRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class GoldenSetIncorrectAnswersRate(ComparableRuleCondition):
    """The percentage of incorrect responses in control tasks
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class GoldenSetIncorrectAnswersRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class IncomeSumForLast24Hours(ComparableRuleCondition):
    """The performer earnings for completed tasks in the pool over the last 24 hours
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class IncomeSumForLast24Hours.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class IncorrectAnswersRate(ComparableRuleCondition):
    """The percentage of incorrect responses

    Be careful, it may have different meanings in different collectors.
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class IncorrectAnswersRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class NextAssignmentAvailable(ComparableRuleCondition):
    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class NextAssignmentAvailable.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[bool]


class PendingAssignmentsCount(ComparableRuleCondition):
    """Number of Assignments pending checking
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class PendingAssignmentsCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class PoolAccessRevokedReason(IdentityRuleCondition):
    """Reason for loss of access of the performer to the current pool

    Attributes:
        value: exact reason
            * SKILL_CHANGE - The performer no longer meets one or more filters.
            * RESTRICTION - The performer's access to tasks is blocked by a quality control rule (such as control tasks,
                majority vote, fast answers, skipped assignments, or captcha).
    """

    class Type(Enum):
        """An enumeration.
        """

        SKILL_CHANGE = 'SKILL_CHANGE'
        RESTRICTION = 'RESTRICTION'

    def __init__(
        self,
        operator: IdentityOperator,
        value: Optional[Type] = None
    ) -> None:
        """Method generated by attrs for class PoolAccessRevokedReason.
        """
        ...

    operator: IdentityOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[Type]


class RejectedAssignmentsCount(ComparableRuleCondition):
    """How many times this assignment was rejected
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class RejectedAssignmentsCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class RejectedAssignmentsRate(ComparableRuleCondition):
    """Percentage of how many assignments were rejected from this performer out of all checked assignment
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class RejectedAssignmentsRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class SkillId(IdentityRuleCondition):
    """The performer no longer meets the specific skill filter
    """

    def __init__(
        self,
        operator: IdentityOperator,
        value: Optional[str] = None
    ) -> None:
        """Method generated by attrs for class SkillId.
        """
        ...

    operator: IdentityOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[str]


class SkippedInRowCount(ComparableRuleCondition):
    """How many tasks in a row the performer skipped
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class SkippedInRowCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class StoredResultsCount(ComparableRuleCondition):
    """How many times the performer entered captcha
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class StoredResultsCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class SubmittedAssignmentsCount(ComparableRuleCondition):
    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class SubmittedAssignmentsCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class SuccessRate(ComparableRuleCondition):
    """Percentage of correct answers of the performer to the captcha
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = None
    ) -> None:
        """Method generated by attrs for class SuccessRate.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[float]


class TotalAnswersCount(ComparableRuleCondition):
    """The number of completed tasks by the performer

    Be careful, it may have different meanings in different collectors.
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class TotalAnswersCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class TotalAssignmentsCount(ComparableRuleCondition):
    """How many assignments from this performer were checked
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class TotalAssignmentsCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]


class TotalSubmittedCount(ComparableRuleCondition):
    """The number of assignments a specific performer completed
    """

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class TotalSubmittedCount.
        """
        ...

    operator: CompareOperator
    _unexpected: Optional[Dict[str, Any]]
    value: Optional[int]
