describe('template spec', () => {
  beforeEach(() => {
    cy.viewport(2048, 1043);

    cy.visit(Cypress.env("CYPRESS_BASE_URL"));
    cy.wait(1000);

    cy.get('#user_code').type(Cypress.env("CYPRESS_USERNAME"));
    cy.wait(1000);

    cy.get('#password').type(
      Cypress.env("CYPRESS_PASSWORD")
    );
    cy.wait(1000);
    cy.get("#login-button").click();
    cy.wait(1000);
    cy.url().should("include", "/home");
  });
  it('passes', () => {
    cy.visit('https://example.cypress.io')
  })
})