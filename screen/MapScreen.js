import React, { useState } from 'react';
import {View, StyleSheet} from 'react-native';
import MapView from 'react-native-maps';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';
import Constants from 'expo-constants';


const MapScreen = () => {

  const [lat, setlat] = useState();
  const [lng, setlng] = useState(); 
  const MapHelper = async () => {
    const result = await Permissions.askAsync(Permissions.LOCATION);
      const location = await Location.getCurrentPositionAsync({
        timeout: 10000
      });
      const lat = location.coords.latitude;
      const lng = location.coords.longitude;
      setlat(lat);
      setlng(lng) 
  };
  return(
    <View style={styles.container}>
    <MapView style={styles.map} region={{
    latitude: 23.4168045,
    longitude: 85.4380671,
    latitudeDelta: 0.0122,
    longitudeDelta: 0.0121}} >
    <MapView.Marker coordinate={{
      latitude: 23.4168045, 
      longitude: 85.4380671
      }} title='User' description="User" />
    </MapView>
  </View>
  )
}


const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 3,
    bottom: 0,
    left: 0,
    right: 0,
    justifyContent: 'flex-end',
    alignItems: 'center'
  },
  map: {
    position: 'absolute',
    top: 3,
    bottom: 0,
    left: 0,
    right: 0 
  }
})

export default MapScreen;