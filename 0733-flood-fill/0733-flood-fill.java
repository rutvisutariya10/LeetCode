class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original_color = image[sr][sc];
        image[sr][sc] = color;
        int[] x_coord = {sr,sr,sr-1,sr+1};
        int[] y_coord = {sc-1,sc+1,sc,sc};
        List<Integer> to_explore = new ArrayList<Integer>();
        for(int i = 0; i < 4; i++){
            int x = x_coord[i], y = y_coord[i];
            if((x > -1) && (y > -1) && (x < image.length) && (y < image[0].length) && (image[x][y] == original_color) && (image[x][y] != color)){
                to_explore.add(i);
            }
        }
        for(Integer i: to_explore){
            image = floodFill(image,x_coord[i],y_coord[i],color);
            image[x_coord[i]][y_coord[i]] = color;
        }
       return image; 
    }
}