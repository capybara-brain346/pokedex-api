pm.test("Response status code is 200", function () {
  pm.expect(pm.response.code).to.equal(200);
});

pm.test("Response time is less than 200ms", function () {
  pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Validate the response schema for required fields", function () {
  const responseData = pm.response.json();

  pm.expect(responseData).to.be.an("object");
  const requiredFields = [
    "name",
    "type",
    "species",
    "height",
    "weight",
    "abilities",
    "catch_rate",
    "base_friendship",
    "base_exp",
    "growth_rate",
    "gender",
    "hp",
    "attack",
    "defense",
    "sp_attack",
    "sp_defense",
    "speed",
  ];

  requiredFields.forEach(function (field) {
    pm.expect(responseData).to.have.property(field);
  });
});
