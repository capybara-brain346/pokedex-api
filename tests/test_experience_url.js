pm.test("Response status code is 200", function () {
    pm.response.to.have.status(200);
});


pm.test("Response time is less than 200ms", function () {
  pm.expect(pm.response.responseTime).to.be.below(200);
});


pm.test("Validate the schema of the response", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData).to.have.property('0').that.is.an('object');
    
    const requiredFields = ['name', 'type', 'species', 'height', 'weight', 'abilities', 'catch_rate', 'base_friendship', 'base_exp', 'growth_rate', 'gender', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed'];
    
    requiredFields.forEach(field => {
        pm.expect(responseData['0']).to.have.property(field);
    });
    
    pm.expect(responseData['0'].name).to.be.a('string');
    pm.expect(responseData['0'].type).to.be.a('string');
    pm.expect(responseData['0'].species).to.be.a('string');
    pm.expect(responseData['0'].height).to.be.a('number');
    pm.expect(responseData['0'].weight).to.be.a('number');
    pm.expect(responseData['0'].abilities).to.be.a('string');
    pm.expect(responseData['0'].catch_rate).to.be.a('number');
    pm.expect(responseData['0'].base_friendship).to.be.a('number');
    pm.expect(responseData['0'].base_exp).to.be.a('number');
    pm.expect(responseData['0'].growth_rate).to.be.a('string');
    pm.expect(responseData['0'].gender).to.be.a('string');
    pm.expect(responseData['0'].hp).to.be.a('number');
    pm.expect(responseData['0'].attack).to.be.a('number');
    pm.expect(responseData['0'].defense).to.be.a('number');
    pm.expect(responseData['0'].sp_attack).to.be.a('number');
    pm.expect(responseData['0'].sp_defense).to.be.a('number');
    pm.expect(responseData['0'].speed).to.be.a('number');
});
