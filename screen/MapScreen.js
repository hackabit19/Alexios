import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

// navigator.geolocation.getCurrentPosition(
//   position => {
//     console.log(position);
//   }
// )

const MapScreen = props => {
    return(
        <View style={styles.container}>
            <Text>MapScreen</Text>
        </View>
    )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default MapScreen;
