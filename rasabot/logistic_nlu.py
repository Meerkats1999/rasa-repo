import os
import typing
from typing import Any, Optional, Text, Dict, List, Type, Tuple

import numpy as np
import pandas as pd

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import TrainingData, Message
from rasa.nlu.featurizers.featurizer import sequence_to_sentence_features
from rasa.nlu.constants import DENSE_FEATURE_NAMES, TEXT

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class LogisticClassifier(Component):
    """A new component"""

    # Which components are required by this component.
    # Listed components should appear before the component itself in the pipeline.
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        """Specify which components need to be present in the pipeline."""

        return []

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {}

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    supported_language_list = None

    # Defines what language(s) this component can NOT handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    not_supported_language_list = None

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)
        #self.le = LabelEncoder()
        self.clf = LogisticRegression(random_state = 0) #You can try to fit your own model

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.train`
        of components previous to this one."""
        # labels = [e.get("intent") for e in training_data.intent_examples]

        
        # y = self.transform_labels_str2num(labels)
        # X = np.stack(
        #     [
        #         sequence_to_sentence_features(
        #             example.get(DENSE_FEATURE_NAMES[TEXT])
        #             )
        #         for example in training_data.intent_examples
        #     ]
        # )
        #     # reduce dimensionality
        # X = np.reshape(X, (len(X), -1))

        # self.clf.fit(X, y)

        dataset = pd.read_csv('/home/abhrajyoti/stuff/rasa-tut/Social_Network_Ads.csv')
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values

        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X)
        X_test = sc.transform(X)

        self.clf.fit(X_train, y)


    def transform_labels_str2num(self, labels: List[Text]) -> np.ndarray:
        return self.le.fit_transform(labels)

    def transform_labels_num2str(self, y: np.ndarray) -> np.ndarray:
        return self.le.inverse_transform(y)

    #Modi please write the next three functions
    def process(self, message: Message, **kwargs: Any) -> None:
        """Process an incoming message.

        This is the components chance to process an incoming
        message. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.process`
        of components previous to this one."""
        pass

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""
        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
