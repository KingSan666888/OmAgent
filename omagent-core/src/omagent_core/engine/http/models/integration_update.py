import pprint
import re  # noqa: F401

import six


class IntegrationUpdate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "category": "str",
        "configuration": "dict(str, object)",
        "description": "str",
        "enabled": "bool",
        "type": "str",
    }

    attribute_map = {
        "category": "category",
        "configuration": "configuration",
        "description": "description",
        "enabled": "enabled",
        "type": "type",
    }

    def __init__(
        self,
        category=None,
        configuration=None,
        description=None,
        enabled=None,
        type=None,
    ):  # noqa: E501
        """IntegrationUpdate - a model defined in Swagger"""  # noqa: E501
        self._category = None
        self._configuration = None
        self._description = None
        self._enabled = None
        self._type = None
        self.discriminator = None
        if category is not None:
            self.category = category
        if configuration is not None:
            self.configuration = configuration
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if type is not None:
            self.type = type

    @property
    def category(self):
        """Gets the category of this IntegrationUpdate.  # noqa: E501


        :return: The category of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this IntegrationUpdate.


        :param category: The category of this IntegrationUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["API", "AI_MODEL", "VECTOR_DB", "RELATIONAL_DB"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}".format(  # noqa: E501
                    category, allowed_values
                )
            )

        self._category = category

    @property
    def configuration(self):
        """Gets the configuration of this IntegrationUpdate.  # noqa: E501


        :return: The configuration of this IntegrationUpdate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this IntegrationUpdate.


        :param configuration: The configuration of this IntegrationUpdate.  # noqa: E501
        :type: dict(str, object)
        """

        self._configuration = configuration

    @property
    def description(self):
        """Gets the description of this IntegrationUpdate.  # noqa: E501


        :return: The description of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntegrationUpdate.


        :param description: The description of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this IntegrationUpdate.  # noqa: E501


        :return: The enabled of this IntegrationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IntegrationUpdate.


        :param enabled: The enabled of this IntegrationUpdate.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def type(self):
        """Gets the type of this IntegrationUpdate.  # noqa: E501


        :return: The type of this IntegrationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntegrationUpdate.


        :param type: The type of this IntegrationUpdate.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(IntegrationUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IntegrationUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
