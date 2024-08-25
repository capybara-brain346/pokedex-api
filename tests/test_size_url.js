pm.test("Response status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response time is less than 200ms", function () {
  pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Validate the response schema for each pokemon object", function () {
  const responseData = pm.response.json();

  pm.expect(responseData).to.be.an("object");

  Object.values(responseData).forEach((pokemon) => {
    pm.expect(pokemon).to.have.property("name").that.is.a("string");
    pm.expect(pokemon).to.have.property("type").that.is.a("string");
    pm.expect(pokemon).to.have.property("species").that.is.a("string");
    pm.expect(pokemon).to.have.property("height").that.is.a("number");
    pm.expect(pokemon).to.have.property("weight").that.is.a("number");
    pm.expect(pokemon).to.have.property("abilities").that.is.a("string");
    pm.expect(pokemon).to.have.property("catch_rate").that.is.a("number");
    pm.expect(pokemon).to.have.property("base_friendship").that.is.a("number");
    pm.expect(pokemon).to.have.property("base_exp").that.is.a("number");
    pm.expect(pokemon).to.have.property("growth_rate").that.is.a("string");
    pm.expect(pokemon).to.have.property("gender").that.is.a("string");
    pm.expect(pokemon).to.have.property("hp").that.is.a("number");
    pm.expect(pokemon).to.have.property("attack").that.is.a("number");
    pm.expect(pokemon).to.have.property("defense").that.is.a("number");
    pm.expect(pokemon).to.have.property("sp_attack").that.is.a("number");
    pm.expect(pokemon).to.have.property("sp_defense").that.is.a("number");
    pm.expect(pokemon).to.have.property("speed").that.is.a("number");
  });
});
