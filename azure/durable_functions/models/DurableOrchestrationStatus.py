from datetime import datetime
from dateutil.parser import parse as dt_parse
from typing import Any, List
import json

from .OrchestrationRuntimeStatus import OrchestrationRuntimeStatus


class DurableOrchestrationStatus:
    """Represents the status of a durable orchestration instance.

    Can be fetched using [[DurableOrchestrationClient]].[[get_status]].
    """

    # parameter names are as defined by JSON schema and do not conform to PEP8 naming conventions
    # noinspection PyPep8Naming,PyShadowingBuiltins
    def __init__(self, name: str = None, instanceId: str = None, createdTime: str = None,
                 lastUpdatedTime: str = None, input: Any = None, output: Any = None,
                 runtimeStatus: str = None, customStatus: Any = None, history: List[Any] = None,
                 **kwargs):
        self._name: str = name
        self._instance_id: str = instanceId
        self._created_time: datetime = dt_parse(createdTime)
        self._last_updated_time: datetime = dt_parse(lastUpdatedTime)
        self._input: Any = input
        self._output: Any = output
        self._runtime_status: OrchestrationRuntimeStatus = runtimeStatus
        self._custom_status: Any = customStatus
        self._history: List[Any] = history
        if kwargs is not None:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    @classmethod
    def from_json(cls, json_string: str):
        """Convert the value passed into a new instance of the class.

        Parameters
        ----------
        json_string: str
            Context passed a JSON serializable value to be converted into an instance of the class

        Returns
        -------
        DurableOrchestrationStatus
            New instance of the durable orchestration status class
        """
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    @property
    def name(self) -> str:
        """Get the orchestrator function name."""
        return self._name

    @property
    def instance_id(self) -> str:
        """Get the unique ID of the instance.

        The instance ID is generated and fixed when the orchestrator
        function is scheduled. It can either auto-generated, in which case
        it is formatted as a UUID, or it can be user-specified with any
        format.
        """
        return self._instance_id

    @property
    def created_time(self) -> datetime:
        """Get the time at which the orchestration instance was created.

        If the orchestration instance is in the [[Pending]] status, this
        time represents the time at which the orchestration instance was
        scheduled.
        """
        return self._created_time

    @property
    def last_updated_time(self) -> datetime:
        """Get the time at which the orchestration instance last updated its execution history."""
        return self._last_updated_time

    @property
    def input_(self) -> Any:
        """Get the input of the orchestration instance."""
        return self._input

    @property
    def output(self) -> Any:
        """Get the output of the orchestration instance."""
        return self._output

    @property
    def runtime_status(self) -> OrchestrationRuntimeStatus:
        """Get the runtime status of the orchestration instance."""
        return self._runtime_status

    @property
    def custom_status(self) -> Any:
        """Get the custom status payload (if any).

        Set by [[DurableOrchestrationContext]].[[set_custom_status]].
        """
        return self._custom_status

    @property
    def history(self) -> List[Any]:
        """Get the execution history of the orchestration instance.

        The history log can be large and is therefore `undefined` by
        default. It is populated only when explicitly requested in the call
        to [[DurableOrchestrationClient]].[[get_status]].
        """
        return self._history
