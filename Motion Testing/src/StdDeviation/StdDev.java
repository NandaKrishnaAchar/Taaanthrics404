package StdDeviation;

public class StdDev {
	public static void main(String[] args) {
		double [] numArrayX;
        double[] numArrayY;
        double[] numArrayZ ;
        while(true)
        {
        	Thread.sleep(300000);
        	int totalTime=50000;
        	long startTime=System.nanoTime();
        	boolean toFinish=false;
        	int i=0;
        	while(!toFinish)
        	{
        		numArrayX.add(abs(event.values[0]));
        		numArrayY.add(abs(event.values[1]));
        		numArrayZ.add(abs(event.values[2]));
        		toFinish=(System.nanoTime()-startTime >= totalTime);
        	}
        	double SDX = calculateSD(numArrayX);
            double SDY = calculateSD(numArrayY);
            double SDZ = calculateSD(numArrayY);
            System.out.format("Standard Deviation = %.6f,%.6f,%.6f",SDX,SDY,SDZ);
            if(SDX<1 && SDY<1 && SDZ<1)
            {
            	//Constant
            	//don't send notifications
            }
            else if(SDX<3 && SDY<3 && SDZ<1)
            {
            	//Walking
            	//don't send notifications
            }
            else if(SDX>1 && SDY>1 && SDZ>1)
            {
            	//Jogging
            	//don't send notifications
            }
            else if(SDX>3 && SDY>3)
            {
            	//Car
            	//Send notifications
            }
            else if( SDY>1 && SDZ>1 ){
            	//Chatting
            }

        	
        }
            }

    public static double calculateSD(double numArray[])
    {
        double sum = 0.0, standardDeviation = 0.0;
        int length = numArray.length;

        for(double num : numArray) {
            sum += num;
        }

        double mean = sum/length;

        for(double num: numArray) {
            standardDeviation += Math.pow(num - mean, 2);
        }

        return Math.sqrt(standardDeviation/length);
    }
}

