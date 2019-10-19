import React from 'react';
import { createMaterialBottomTabNavigator } from 'react-navigation-material-bottom-tabs';
import { createSwitchNavigator, createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import Icon from 'react-native-vector-icons/Ionicons';
import HomeScreen from '../screen/HomeScreen';
import MapScreen from '../screen/MapScreen';
import EmergencyScreen from '../screen/EmergencyScreen';
import Login from '../screen/Login';
import SignUp from '../screen/SignUp'

const RouteConfings = {
    Home: {screen: HomeScreen, navigationOptions: {
        tabBarLabel: 'Home',
        tabBarIcon: ({ tintColor }) => (<Icon style={[{color: tintColor}]} size={25} name={'md-person'}/>)}},
    Map: {screen: MapScreen, navigationOptions: {
        tabBarLabel: 'Location',
        tabBarIcon: ({ tintColor }) => (<Icon style={[{color: tintColor}]} size={25} name={'ios-map'}/>)}},
    Video: {screen: EmergencyScreen, navigationOptions: {
        tabBarLabel: 'Emergency',
        tabBarIcon: ({ tintColor }) => (<Icon style={[{color: tintColor}]} size={25} name={'ios-alert'}/>)}}
}


const TabNavigator = createMaterialBottomTabNavigator( RouteConfings,
{
        activeColor: '#f0edf6',
        inactiveColor:  '#006400',
        barStyle: { backgroundColor: '#32cd32' } 
});

const MainNavigator = createSwitchNavigator({
        Login: {screen: Login},
        SignUp: {screen: SignUp},
        Main: TabNavigator
    },
    {
        initialRouteName: 'Login'
    }

);

export default createAppContainer(MainNavigator);