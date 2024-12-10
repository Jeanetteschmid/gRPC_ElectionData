
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
public class client {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()
                .build();

        ElectiondataGrpc.ElectiondataBlockingStub stub = ElectiondataGrpc.newBlockingStub(channel);

        ElectiondataOuterClass.MessageRequest request = ElectiondataOuterClass.MessageRequest.newBuilder()
                .setRegionID("123")
                .build();

        ElectiondataOuterClass.MessageResponse response = stub.getElectionData(request);
        System.out.println("Received Data: " + response);

        channel.shutdown();
    }
}
