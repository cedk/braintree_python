from braintree.attribute_getter import AttributeGetter

class DisputePayPalMessage(AttributeGetter):
    def __init__(self, attributes):
        AttributeGetter.__init__(self, attributes)
