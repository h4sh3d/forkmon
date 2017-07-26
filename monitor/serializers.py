from rest_framework import serializers
from .models import *


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = (
            'name', 
            'url', 
            'best_block_hash', 
            'best_block_height', 
            'prev_block_hash',
            'has_reorged',
            'is_behind',
            'is_up',
            'highest_divergence',
            'highest_diverged_hash',
            'stats_node',
            'mtp',
        )


class BIP9ForkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BIP9Fork
        fields = (
            'name',
            'state',
            'count',
            'elapsed',
            'period',
            'threshold',
            'since',
            'current',
        )


class MTForkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MTFork
        fields = (
            'name',
            'activation_time',
        )


class ForkStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForkState
        fields = (
            'has_forked',
            'is_currently_forked',
        )

