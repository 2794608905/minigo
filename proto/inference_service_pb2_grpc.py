# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import inference_service_pb2 as proto_dot_inference__service__pb2


class InferenceServiceStub(object):
  """TODO(tommadams): Investigate enabling arenas with:
  option cc_enable_arenas = true;

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_unary(
        '/minigo.InferenceService/GetConfig',
        request_serializer=proto_dot_inference__service__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=proto_dot_inference__service__pb2.GetConfigResponse.FromString,
        )
    self.GetFeatures = channel.unary_unary(
        '/minigo.InferenceService/GetFeatures',
        request_serializer=proto_dot_inference__service__pb2.GetFeaturesRequest.SerializeToString,
        response_deserializer=proto_dot_inference__service__pb2.GetFeaturesResponse.FromString,
        )
    self.PutOutputs = channel.unary_unary(
        '/minigo.InferenceService/PutOutputs',
        request_serializer=proto_dot_inference__service__pb2.PutOutputsRequest.SerializeToString,
        response_deserializer=proto_dot_inference__service__pb2.PutOutputsResponse.FromString,
        )


class InferenceServiceServicer(object):
  """TODO(tommadams): Investigate enabling arenas with:
  option cc_enable_arenas = true;

  """

  def GetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeatures(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutOutputs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InferenceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=proto_dot_inference__service__pb2.GetConfigRequest.FromString,
          response_serializer=proto_dot_inference__service__pb2.GetConfigResponse.SerializeToString,
      ),
      'GetFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeatures,
          request_deserializer=proto_dot_inference__service__pb2.GetFeaturesRequest.FromString,
          response_serializer=proto_dot_inference__service__pb2.GetFeaturesResponse.SerializeToString,
      ),
      'PutOutputs': grpc.unary_unary_rpc_method_handler(
          servicer.PutOutputs,
          request_deserializer=proto_dot_inference__service__pb2.PutOutputsRequest.FromString,
          response_serializer=proto_dot_inference__service__pb2.PutOutputsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'minigo.InferenceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))