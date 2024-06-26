import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './src/screens/HomeScreen';
import AccelerometerDataScreen from './src/screens/AccelerometerDataScreen';
import ReadCSVScreen from './src/screens/CSVScreen';
import CollectedData from './src/screens/DataCollectorScreen';
import AboutUs from './src/screens/AboutUs';
import axios from 'axios'
const Stack = createStackNavigator();
console.disableYellowBox = true;
const App = () => {
  const [data, setData] = React.useState([]);

  React.useEffect(() => {
      async function fetchData() {
          try {
              const response = await axios.get('http://192.168.52.74:5000/api/getdata');
              setData(response.data.message);
          } catch (error) {
              console.error('Error fetching data:', error);
          }
      }
 
      fetchData();
  }, []);
  console.log(data)
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: 'Home' }} />
        <Stack.Screen name="AccelerometerData" component={AccelerometerDataScreen} options={{ title: 'Accelerometer Data' }} />
        <Stack.Screen name="ReadCSV" component={ReadCSVScreen} options={{ title: 'CSV Data' }}/>
        <Stack.Screen name="CollectData" component={CollectedData} options={{ title: 'Collect Data' }}/>
        <Stack.Screen name="AccelerometerDatabase" component={AccelerometerDataScreen} options={{title : 'Accelerometer Data'}}/>
        <Stack.Screen name="AboutUs" component={AboutUs} options={{title : 'About Us'}}/>
        
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;